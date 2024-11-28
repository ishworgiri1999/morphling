#!/bin/bash

set -e

CONTROLLER_IMG=ishworgiri/morphling-controllers:latest
DB_MANAGER_IMG=ishworgiri/morphling-database-manager:latest
UI_IMG=ishworgiri/morphling-ui:latest
ALGORITHM_IMG=ishworgiri/morphling-algorithm:base
CLIENT_IMG=ishworgiri/morphling-http-client:faas

SCRIPT_ROOT=$(dirname ${BASH_SOURCE})/..
cd ${SCRIPT_ROOT}
echo "cd to ${SCRIPT_ROOT}"

# controller, storage, and ui
docker push ${UI_IMG}
docker push ${DB_MANAGER_IMG}
docker push ${CONTROLLER_IMG}

# algorithm server
docker push ${ALGORITHM_IMG}

# http client
docker push ${CLIENT_IMG}

echo -e "\n Docker images push succeeded\n"
