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
IMAGE_TAG="v$(date +%s)"
docker build -t kv-frontend:latest -f Dockerfile.service . | tee -a "$OUTPUT_FILE"
docker build -t kv-storage:latest -f Dockerfile.storage . | tee -a "$OUTPUT_FILE"
docker build --build-arg CACHEBUST="$IMAGE_TAG" -t kv-controller:latest -t kv-controller:$IMAGE_TAG -f Dockerfile.controller . | tee -a "$OUTPUT_FILE"

log "## 2. Deploying to Kubernetes"
kubectl apply -f k8s/ | tee -a "$OUTPUT_FILE"

log "Restarting deployments to pick up new images..."
kubectl rollout restart deployment frontend || true
kubectl set image deployment/controller controller=kv-controller:$IMAGE_TAG
kubectl rollout restart statefulset storage || true

log "Waiting for pods to be ready (this may take a minute)..."
kubectl wait --for=condition=ready pod -l app=frontend --timeout=120s
kubectl wait --for=condition=ready pod -l app=storage --timeout=120s
kubectl wait --for=condition=ready pod -l app=controller --timeout=120s

