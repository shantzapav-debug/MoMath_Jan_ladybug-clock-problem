#!/usr/bin/env bash
# Launches the Streamlit dashboard from the virtualenv created by install.sh.
# Used as the Cloud Agent `terminals` command so the app runs on every boot.
set -euo pipefail

cd "$(dirname "$0")/.."
VENV_DIR="${LADYBUG_VENV:-$HOME/.venvs/ladybug-clock}"

exec "$VENV_DIR/bin/streamlit" run streamlit_dashboard.py \
  --server.port 8501 \
  --server.address 0.0.0.0 \
  --server.headless true
