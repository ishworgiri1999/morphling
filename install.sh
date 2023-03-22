kubectl apply -f config/crd/bases/tuning.kubedl.io_trials.yaml
kubectl apply -f config/crd/bases/tuning.kubedl.io_profilingexperiments.yaml

kubectl create namespace morphling-system
kubectl apply -k manifests/configmap
kubectl apply -k manifests/controllers
kubectl apply -k manifests/pv
kubectl apply -k manifests/mysql-db
kubectl apply -k manifests/db-manager
kubectl apply -k manifests/ui
kubectl apply -k manifests/algorithm
