#!/usr/bin/env bash
# Idempotent environment bootstrap for the Ladybug Clock Problem dashboard.
# Runs after the repository is checked out. Safe to run repeatedly.
#
# The virtualenv is created OUTSIDE the repository working tree so it survives
# the fresh git checkout that happens when a Cloud Agent boots from a prebuilt
# environment (an in-repo, untracked .venv would be cleaned away).
set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
VENV_DIR="${LADYBUG_VENV:-$HOME/.venvs/ladybug-clock}"

# python3-venv is required to create the virtual environment on the base image.
if ! python3 -c "import ensurepip" >/dev/null 2>&1; then
  sudo apt-get update
  sudo apt-get install -y python3-venv
fi

# Create the virtual environment if it does not already exist.
if [ ! -x "$VENV_DIR/bin/python" ]; then
  python3 -m venv "$VENV_DIR"
fi

"$VENV_DIR/bin/python" -m pip install --upgrade pip
"$VENV_DIR/bin/pip" install -r "$REPO_DIR/requirements.txt"

echo "Environment ready. Virtualenv: $VENV_DIR"
