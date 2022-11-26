#!/bin/bash

set -e

PWD=$(pwd)

if [ "$#" -ne 2 ]; then
    echo "USAGE: bin/run.sh <in_file_path> <out_file_path>"
    exit 1
fi

input=$1
output=$2

python "$PWD"/src/main.py "$input" "$output"

exit 0