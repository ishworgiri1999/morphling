module github.com/alibaba/morphling

go 1.16

require (
	github.com/Interstellarss/faas-share v0.0.0-00010101000000-000000000000
	github.com/ghodss/yaml v1.0.0
	github.com/gin-contrib/sessions v0.0.3
	github.com/gin-contrib/static v0.0.1
	github.com/gin-gonic/gin v1.7.2
	github.com/go-logr/logr v1.2.3
	github.com/go-sql-driver/mysql v1.6.0
	github.com/golang/mock v1.6.0
	github.com/golang/protobuf v1.5.2
	github.com/jinzhu/gorm v1.9.16
	github.com/jinzhu/now v1.1.2 // indirect
	github.com/mattn/go-sqlite3 v2.0.1+incompatible // indirect
	github.com/onsi/gomega v1.24.1 // indirect
	github.com/stretchr/testify v1.8.0
	golang.org/x/net v0.3.1-0.20221206200815-1e63c2f08a10
	google.golang.org/grpc v1.43.0
	google.golang.org/protobuf v1.28.1
	k8s.io/api v0.26.0
	k8s.io/apimachinery v0.26.0
	k8s.io/apiserver v0.24.2
	k8s.io/client-go v0.26.0
	k8s.io/klog v1.0.0
	sigs.k8s.io/controller-runtime v0.12.0
)

replace (
	k8s.io/api => k8s.io/api v0.24.2
	k8s.io/apiextensions-apiserver => k8s.io/apiextensions-apiserver v0.24.2
	k8s.io/apimachinery => k8s.io/apimachinery v0.24.5-rc.0
	k8s.io/apiserver => k8s.io/apiserver v0.24.2
	k8s.io/cli-runtime => k8s.io/cli-runtime v0.24.2
	k8s.io/client-go => k8s.io/client-go v0.24.2
	k8s.io/cloud-provider => k8s.io/cloud-provider v0.24.2
	k8s.io/cluster-bootstrap => k8s.io/cluster-bootstrap v0.24.2
	k8s.io/component-base => k8s.io/component-base v0.24.2
	k8s.io/cri-api => k8s.io/cri-api v0.25.0-alpha.0
	k8s.io/csi-translation-lib => k8s.io/csi-translation-lib v0.24.2
	k8s.io/kube-aggregator => k8s.io/kube-aggregator v0.24.2
	k8s.io/kube-controller-manager => k8s.io/kube-controller-manager v0.24.2
	k8s.io/kube-proxy => k8s.io/kube-proxy v0.24.2
	k8s.io/kube-scheduler => k8s.io/kube-scheduler v0.24.2
	k8s.io/kubectl => k8s.io/kubectl v0.24.2
	k8s.io/kubelet => k8s.io/kubelet v0.24.2
	k8s.io/legacy-cloud-providers => k8s.io/legacy-cloud-providers v0.24.2
	k8s.io/metrics => k8s.io/metrics v0.24.2
	k8s.io/node-api => k8s.io/node-api v0.18.5
	k8s.io/sample-apiserver => k8s.io/sample-apiserver v0.24.2
	k8s.io/sample-cli-plugin => k8s.io/sample-cli-plugin v0.24.2
	k8s.io/sample-controller => k8s.io/sample-controller v0.24.2
)

//replace
//k8s.io/api => k8s.io/api v0.18.6
replace k8s.io/code-generator => k8s.io/code-generator v0.24.7-rc.0

replace k8s.io/component-helpers => k8s.io/component-helpers v0.24.2

replace k8s.io/controller-manager => k8s.io/controller-manager v0.24.2

replace k8s.io/mount-utils => k8s.io/mount-utils v0.24.7-rc.0

replace k8s.io/pod-security-admission => k8s.io/pod-security-admission v0.24.2

replace github.com/Interstellarss/faas-share => github.com/Interstellarss/faas-share v0.1.23

//replace github.com/go-logr/logr => github.com/go-logr/logr v0.2.0

replace github.com/onsi/gomega => github.com/onsi/gomega v1.8.1

//replace sigs.k8s.io/controller-runtime => github.com/YukioZzz/controller-runtime v0.9.2-logrv1
