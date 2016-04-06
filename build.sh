#!/usr/bin/env bash
#
# Author: Anand Nevase <anand.nevase@xoriant.com>
#
# Build TechX Calculator deliverables.


# Get the app root directory
SCRIPT_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
ROOT_DIR=$( cd "$SCRIPT_DIR/" && pwd )

echo "Removing previous build directories..."
rm -rf "$ROOT_DIR/build"
rm -rf "$ROOT_DIR/TechX-Calculator.egg-info"

#$ROOT_DIR/xperience/xporter/web/build-production.sh || exit 1

echo "Creating egg..."
cd $ROOT_DIR && python setup.py bdist_egg --exclude-source-files || exit 1

echo "Removing temporary files"
rm -rf "$ROOT_DIR/build"
rm -rf "$ROOT_DIR/TechX-Calculator.egg-info"

DIST_PATH="$ROOT_DIR/dist"

echo "Egg Created Successfully at: $DIST_PATH"
