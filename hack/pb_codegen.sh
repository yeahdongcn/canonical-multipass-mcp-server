#!/usr/bin/env bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJ_DIR="$(realpath "${SCRIPT_DIR}"/..)"
VENV_PATH="${PROJ_DIR}/.venv"

source "${VENV_PATH}/bin/activate"

PY_PACKAGE_DIR="${PROJ_DIR}"

uv run -- python -m grpc_tools.protoc \
  -I"canonical_multipass_mcp=${PROJ_DIR}/proto" \
  --python_out="${PY_PACKAGE_DIR}" \
  --pyi_out="${PY_PACKAGE_DIR}" \
  --grpc_python_out="${PY_PACKAGE_DIR}" \
  "${PROJ_DIR}"/proto/*.proto
