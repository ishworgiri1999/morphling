
# Image URL to use all building/pushing image targets
CONTROLLER_IMG ?= ishworgiri/morphling-controllers:latest
DB_MANAGER_IMG ?= ishworgiri/morphling-database-manager:latest
UI_IMG ?= ishworgiri/morphling-ui:latest
# Produce CRDs that work back to Kubernetes 1.11 (no version conversion)
CRD_OPTIONS ?= "crd:trivialVersions=true,maxDescLen=0"

# Get the currently used golang install path (in GOPATH/bin, unless GOBIN is set)
ifeq (,$(shell go env GOBIN))
GOBIN=$(shell go env GOPATH)/bin
else
GOBIN=$(shell go env GOBIN)
endif

all: manager

# Run tests
test: generate fmt vet manifests
	go test ./... -coverprofile cover.out

# Build manager binary
manager:  fmt vet
	go build -ldflags "-X google.golang.org/protobuf/reflect/protoregistry conflictPolicy=warn" -o bin/manager cmd/controllers/main.go

# Run against the configured Kubernetes cluster in ~/.kube/config
run: generate fmt vet manifests
	go run cmd/controllers/main.go

# Install CRDs into a cluster
install: manifests
	kustomize build config/crd | kubectl create -f -

# Uninstall CRDs from a cluster
uninstall: manifests
	kustomize build config/crd | kubectl delete -f -

# Deploy controller in the configured Kubernetes cluster in ~/.kube/config
deploy: manifests
	cd config/manager && kustomize edit set image controller=${IMG}
	kustomize build config/default | kubectl create -f -

# Generate manifests e.g. CRD, RBAC etc.
manifests: controller-gen
	$(CONTROLLER_GEN) $(CRD_OPTIONS) rbac:roleName=manager-role webhook paths="./..." output:crd:artifacts:config=config/crd/bases

# Run go fmt against code
fmt:
	go fmt ./...

# Clean code
clean: fmt vet
	bash script/clean_python_code.sh

# Run go vet against code
vet:
	go vet ./...

# Generate code
generate: controller-gen
	$(CONTROLLER_GEN) object:headerFile="hack/boilerplate.go.txt" paths="./..."

# Build the docker image
docker-build: clean
	bash script/docker_build.sh

# Push the docker image
docker-push:
	bash script/docker_push.sh

# find or download controller-gen
# download controller-gen if necessary
controller-gen:
ifeq (, $(shell which controller-gen))
	go get sigs.k8s.io/controller-tools/cmd/controller-gen@v0.4.1
CONTROLLER_GEN=$(GOBIN)/controller-gen
else
CONTROLLER_GEN=$(shell which controller-gen)
endif

# Update helm charts
# For example: export VERSION=0.5.0 && make helm-charts
helm-chart:
	bash script/helm_chart.sh

