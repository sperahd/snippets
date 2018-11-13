## Types of K8s components

### Master components
These are the components that provide cluster's control plane. All the global decisions about the cluster are made by the cluster's control plane. It consists of following

#### kube-apiserver 

Frontend for kubernetes control plane.

#### etcd

Consistent and highly-available key value store used as Kubernetes’ backing store for all cluster data.

#### kube-scheduler

Component on the master that watches newly created pods that have no node assigned, and selects a node for them to run on.

Factors taken into account for scheduling decisions include individual and collective resource requirements, hardware/software/policy constraints, affinity and anti-affinity specifications, data locality, inter-workload interference and deadlines.

#### kube-controller-manager

Component on the master that runs controllers .

Logically, each controller  is a separate process, but to reduce complexity, they are all compiled into a single binary and run in a single process.

These controllers include:

1. Node Controller: Responsible for noticing and responding when nodes go down.
2. Replication Controller: Responsible for maintaining the correct number of pods for every replication controller object in the system.
3. Endpoints Controller: Populates the Endpoints object (that is, joins Services & Pods).
4. Service Account & Token Controllers: Create default accounts and API access tokens for new namespaces.

#### cloud-controller-manager

Runs controllers that interact with the underlying cloud providers. Following controllers have cloud provider dependencies:
1. Node controller - For checking the cloud provider to determine if a node has been deleted in the cloud after it stops responding
2. Route Controller: For setting up routes in the underlying cloud infrastructure
3. Service Controller: For creating, updating and deleting cloud provider load balancers
4. Volume Controller: For creating, attaching, and mounting volumes, and interacting with the cloud provider to orchestrate volumes

### Node components

#### kubelet 

An agent that runs on each node in the cluster. It makes sure that containers are running in a pod.

The kubelet takes a set of PodSpecs that are provided through various mechanisms and ensures that the containers described in those PodSpecs are running and healthy.


#### kube-proxy

kube-proxy enables the Kubernetes service abstraction by maintaining network rules on the host and performing connection forwarding.


#### Container Runtime

The container runtime is the software that is responsible for running containers. Kubernetes supports several runtimes: docker, rkt

### Addons

#### DNS - https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/

#### WebUI - https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/

#### Cluster-level Logging - https://kubernetes.io/docs/concepts/cluster-administration/logging/

#### Container Resource Monitoring - https://kubernetes.io/docs/tasks/debug-application-cluster/resource-usage-monitoring/
