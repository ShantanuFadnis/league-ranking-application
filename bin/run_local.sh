#!/bin/bash

set -e

PWD=$(pwd)

if [ "$#" -ne 2 ]; then
    echo "USAGE: bin/run.sh <in_file_path> <out_file_path>"
    exit 1
fi

input=$1
output=$2

# Activate Python Virtual Environment
source "${PWD}"/venv/bin/activate

# Install Python dependencies using pip
pip install -r "${PWD}"/requirements.txt

# Run application
source ${PWD}/bin/run.sh "${input}" "${output}"

# Deactivate Python Virtual Environment
deactivate

exit 0