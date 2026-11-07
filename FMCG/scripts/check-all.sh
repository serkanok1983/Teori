#!/usr/bin/env bash
# Full QA: validator + integrity checks; writes reports/QA-REPORT.md
set -e
cd "$(dirname "$0")/.."
python3 scripts/check_all.py "$@"
