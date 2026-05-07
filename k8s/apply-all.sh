#!/usr/bin/env bash
set -e

kubectl apply -f backend.yaml
kubectl apply -f controller.yaml
kubectl apply -f frontend.yaml
