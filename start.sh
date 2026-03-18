#!/bin/bash
set -e
echo "Starting Web3 Decentralized Identity Verifier..."
uvicorn app:app --host 0.0.0.0 --port 9145 --workers 1
