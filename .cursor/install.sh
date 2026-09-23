#!/usr/bin/env bash
# Idempotent environment bootstrap for the Ladybug Clock Problem dashboard.
# Runs after the repository is checked out. Safe to run repeatedly.
set -euo pipefail

cd "$(dirname "$0")/.."

# python3-venv is required to create the virtual environment on the base image.
if ! python3 -c "import ensurepip" >/dev/null 2>&1; then
  sudo apt-get update
  sudo apt-get install -y python3-venv
fi

# Create the virtual environment if it does not already exist.
if [ ! -x ".venv/bin/python" ]; then
  python3 -m venv .venv
fi

.venv/bin/python -m pip install --upgrade pip
.venv/bin/pip install -r requirements.txt

echo "Environment ready."
