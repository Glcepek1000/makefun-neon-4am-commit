#!/bin/sh
# One-shot setup: verify Python, run the entry, show the result.
set -e
cd "$(dirname "$0")"
python3 --version
python3 main.py
echo "--- entry.txt ---"
cat "${OUTPUT_DIR:-/output}/entry.txt"
echo
echo "setup complete: zero errors."
