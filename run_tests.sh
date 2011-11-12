#!/bin/bash

set -eu

function usage {
  echo "BATTLE SNAKE"
}

function process_option {
  case "$1" in
    -h|--help) usage;;
    *)
  esac
}

for arg in "$@"; do
  process_option $arg
done

function run_pep8 {
  echo "Running pep8 ..."
  srcfiles=" `find *py`"
  python -m pep8 --repeat --show-pep8 --show-source ${srcfiles}
}

run_pep8
