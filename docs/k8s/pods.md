## Definition

A Pod is the basic building block of Kubernetes–the smallest and simplest unit in the Kubernetes object model that you create or deploy. A Pod represents a running process on your cluster.

### Pod contents

A Pod encapsulates an application container (or, in some cases, multiple containers), storage resources, a unique network IP, and options that govern how the container(s) should run. A Pod represents a unit of deployment: a single instance of an application in Kubernetes, which might consist of either a single container or a small number of containers that are tightly coupled and that share resources.

### Scaling concerns

Each Pod is meant to run a single instance of a given application. If you want to scale your application horizontally (e.g., run multiple instances), you should use multiple Pods, one for each instance. In Kubernetes, this is generally referred to as replication. Replicated Pods are usually created and managed as a group by an abstraction called a Controller.

### Shared context
A pod’s contents are always co-located and co-scheduled, and run in a shared context. The shared context of a pod is a set of Linux namespaces, cgroups, and potentially other facets of isolation - the same things that isolate a Docker container. 
Containers within the pod can communicate with each other using standard inter-process communications like SystemV semaphores or POSIX shared memory or localhost.

### Privileged mode
From Kubernetes v1.1, any container in a pod can enable privileged mode, using the privileged flag on the SecurityContext of the container spec.


## Resource sharing

Pods provide two kinds of shared resources to their constituent containers:
1. Networking - each pod is assigned a unique ip in the node's network namespace. The containers withing the pod can communicate with each other using localhost. 
2. Storage - A Pod can specify a set of shared storage volumes. All containers in the Pod can access the shared volumes, allowing those containers to share data. Volumes also allow persistent data in a Pod to survive in case one of the containers within needs to be restarted.

## Pods and Controllers

A Controller can create and manage multiple Pods for you, handling replication and rollout and providing self-healing capabilities at cluster scope. For example, if a Node fails, the Controller might automatically replace the Pod by scheduling an identical replacement on a different Node.

Some examples of Controllers that contain one or more pods include:

1. Deployment
2. StatefulSet
3. DaemonSet
