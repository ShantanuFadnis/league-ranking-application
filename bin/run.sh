#!/bin/bash

set -e

PWD=$(pwd)
if [ "$#" -ne 2 ]; then
    echo "USAGE: bin/run.sh <in_file_path> <out_file_path>"
    exit 1
fi
in_file=$1
out_file=$2

exec python "$PWD"/src/main.py "$in_file" "$out_file"

exit 0