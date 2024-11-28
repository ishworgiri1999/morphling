#!/bin/bash

set -e
ARCH=linux/amd64
CONTROLLER_IMG=ishworgiri/morphling-controllers:latest
DB_MANAGER_IMG=ishworgiri/morphling-database-manager:latest
UI_IMG=ishworgiri/morphling-ui:latest
ALGORITHM_IMG=ishworgiri/morphling-algorithm:base
CLIENT_IMG=ishworgiri/morphling-http-client:faas

SCRIPT_ROOT=$(dirname ${BASH_SOURCE})/..
cd ${SCRIPT_ROOT}
echo "cd to ${SCRIPT_ROOT}"

# controller, storage, and ui
docker build --platform ${ARCH} -t ${UI_IMG}  -f   console/Dockerfile .
docker build --platform ${ARCH} -t ${DB_MANAGER_IMG} -f  cmd/db-manager/Dockerfile .
docker build --platform ${ARCH} -t ${CONTROLLER_IMG} -f  cmd/controllers/Dockerfile .

# algorithm server
docker build --platform ${ARCH} -t ${ALGORITHM_IMG} -f  cmd/algorithm/grid/Dockerfile .

# http client
cp api/v1alpha1/grpc_proto/grpc_storage/python3/* pkg/client_locust/
cd pkg/client_locust/
docker build --platform ${ARCH} -t ${CLIENT_IMG} -f  ./Dockerfile .

echo -e "\n Docker images build succeeded\n"
