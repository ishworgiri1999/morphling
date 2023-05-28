

# Morphling

Morphling is an auto-configuration framework for
machine learning model serving (inference) on Kubernetes.  Check the [website](http://kubedl.io/tuning/intro/) for details.

Current version of Morpling is dedicated for FaST Framework, to be able to utilze and profile the FaST fine-grain GPU sharing mechanism.
## Getting start quickly
As it is automatically installed via the FaST deployment script, we can easily perform the test via `kubectl`:

There are two kinds of profling, the `normal-profiling-test` usually only have one replica per instance, to profile the different perfomance in different resource configurations; while the `mps-replica-test` are the profiling test for multiple replicas of the same instancs with the same resource configuration to benchmark the mps performance.


### Submit the configuration tuning experiment
```
cd morphling/test
kubectl create -f normal-profiling-test/experiment-resnet-grid.yaml
```

The profiling params could includs the following fields:

- `GPU_QUOTA`: the minimum temporal quota request with range: [0.0, 1.0]
- `QUOTA_LIMIT`: the maximum temporal quota limit with range: [0.0, 1.0]
- `GPU_MEMORY`: the gpu memory limit (Byte)
- `GPU_SM`: the gpu partition percentage limit with range: [1, 100]
- `REPLICA`: the replica of the instance, e.g. 1, 2, ... 

### Monitor the status of the configuration tuning experiment
```bash
kubectl get -n morphling-system pe
kubectl describe -n morphling-system pe
```

#### Monitor sampling trials (performance test)
```bash
kubectl -n morphling-system get trial
```

#### Get the searched optimal configuration
```bash
kubectl -n morphling-system get pe
```

Expected output:
```bash
NAME                        STATE       AGE   OBJECT NAME   OPTIMAL OBJECT VALUE   OPTIMAL PARAMETERS
mobilenet-experiment-grid   Succeeded   12m   qps           32                     [map[category:resource name:cpu value:4] map[category:env name:BATCH_SIZE value:32]]
```

#### Delete the tuning experiment

```bash
kubectl -n morphling-system delete pe --all
```

## Deploy the image manually
### Install using Yaml files

#### Install CRDs

From git root directory, run

```commandline
kubectl apply -k config/crd/bases
```

#### Install Morphling Components
     
```commandline
kubectl create namespace morphling-system

kubectl apply -k manifests/configmap
kubectl apply -k manifests/controllers
kubectl apply -k manifests/pv
kubectl apply -k manifests/mysql-db
kubectl apply -k manifests/db-manager
kubectl apply -k manifests/ui
kubectl apply -k manifests/algorithm
```
By default, Morphling will be installed under `morphling-system` namespace.

The official Morphling component images are hosted under [docker hub](https://hub.docker.com/r/kubedl).

Check if all components are running successfully:
```commandline
kubectl get deployment -n morphling-system
```

Expected output:
```commandline
NAME                         READY   UP-TO-DATE   AVAILABLE   AGE
morphling-algorithm-server   1/1     1            1           34s
morphling-controller         1/1     1            1           9m23s
morphling-db-manager         1/1     1            1           9m11s
morphling-mysql              1/1     1            1           9m15s
morphling-ui                 1/1     1            1           4m53s
```

#### Uninstall Morphling controller

```bash
bash script/undeploy.sh
```

#### Delete CRDs
```bash
kubectl get crd | grep morphling.kubedl.io | cut -d ' ' -f 1 | xargs kubectl delete crd
```

## Developer Guide

#### Build the controller manager binary
Note: please not forget to change the repo name in the `./script`

```bash
make manager
```
#### Run the tests

```bash
make test
```
#### Generate manifests, e.g., CRD, RBAC YAML files, etc.

```bash
make manifests
```
#### Build the component docker images, e.g., Morphling controller, DB-Manager

```bash
make docker-build
```

#### Push the component docker images

```bash
make docker-push
```
