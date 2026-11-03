#!/bin/sh
# Verify the whole example blog: tests, clean build, link checks.
set -e
cd "$(dirname "$0")/.."
python3 tools/test_build.py
python3 tools/build.py --quiet
python3 tools/check.py
echo "All green: tests pass, site builds, links resolve."
