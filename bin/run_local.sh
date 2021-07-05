#!/bin/bash

set -e

PWD=$(pwd)

if [ "$#" -ne 2 ]; then
    echo "USAGE: bin/run_local.sh <in_file_path> <out_file_path>"
    exit 1
fi

input=$1
output=$2

if [ -z "$input" ]; then
    echo "Input file required."
    exit 1
fi

# Create a Virtual Environment
python3 -m venv "${PWD}"/venv

# Activate Python Virtual Environment
source "${PWD}"/venv/bin/activate

# Install Python dependencies using pip
pip install -r "${PWD}"/requirements.txt

# Run application
python "$PWD"/src/main.py "$input" "$output"

# Deactivate Python Virtual Environment
deactivate

exit 0