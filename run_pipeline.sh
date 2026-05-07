#!/bin/bash
set -e

OUTPUT_FILE="test_results.md"

echo "# Distributed Marketplace Pipeline Results" > "$OUTPUT_FILE"
echo "Run Date: $(date)" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

log() {
    echo "$1"
    echo "$1" >> "$OUTPUT_FILE"
}

log "## 1. Building Docker Images"
docker build -t kv-frontend:latest -f Dockerfile.service . | tee -a "$OUTPUT_FILE"
docker build -t kv-storage:latest -f Dockerfile.storage . | tee -a "$OUTPUT_FILE"
docker build -t kv-controller:latest -f Dockerfile.controller . | tee -a "$OUTPUT_FILE"

log "## 2. Deploying to Kubernetes"
kubectl apply -f k8s/ | tee -a "$OUTPUT_FILE"

log "Restarting deployments to pick up new images..."
kubectl rollout restart deployment frontend controller || true
kubectl rollout restart statefulset storage || true

log "Waiting for pods to be ready (this may take a minute)..."
kubectl wait --for=condition=ready pod -l app=frontend --timeout=120s
kubectl wait --for=condition=ready pod -l app=storage --timeout=120s
kubectl wait --for=condition=ready pod -l app=controller --timeout=120s

log "## 3. Setting up Test Environment"
kubectl delete pod test-client --ignore-not-found
kubectl run test-client --image=kv-frontend:latest --image-pull-policy=IfNotPresent --restart=Never -- sleep infinity

log "Waiting for test-client to be ready..."
kubectl wait --for=condition=ready pod/test-client --timeout=60s

log "Copying test scripts to test-client..."
kubectl cp tests/test_client.py test-client:/app/tests/test_client.py
kubectl cp tests/load_test.py test-client:/app/tests/load_test.py
kubectl cp tests/mixed_load_test.py test-client:/app/tests/mixed_load_test.py

log "## 4. Running Integration Tests"
echo '```text' >> "$OUTPUT_FILE"
kubectl exec test-client -- python /app/tests/test_client.py 2>&1 | tee -a "$OUTPUT_FILE"
echo '```' >> "$OUTPUT_FILE"

log "## 5. Running Read-Heavy Load Test (10s, 20 workers)"
echo '```text' >> "$OUTPUT_FILE"
kubectl exec test-client -- python /app/tests/load_test.py --target=frontend:50051 --workers=20 --duration=10 2>&1 | tee -a "$OUTPUT_FILE"
echo '```' >> "$OUTPUT_FILE"

log "## 6. Running Mixed Read/Write Load Test (10s, 20 workers, 10% Bids)"
echo '```text' >> "$OUTPUT_FILE"
kubectl exec test-client -- python /app/tests/mixed_load_test.py --target=frontend:50051 --workers=20 --duration=10 --write-ratio=0.1 2>&1 | tee -a "$OUTPUT_FILE"
echo '```' >> "$OUTPUT_FILE"

log "Pipeline complete! Full results saved to $OUTPUT_FILE"
