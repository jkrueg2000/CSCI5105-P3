#!/usr/bin/env bash
set -e

# Apply the single valid config: frontend.yaml
kubectl apply -f frontend.yaml
