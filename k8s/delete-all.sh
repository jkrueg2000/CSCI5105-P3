#!/usr/bin/env bash
set -e

# Delete the frontend resources defined in frontend.yaml
kubectl delete -f frontend.yaml
