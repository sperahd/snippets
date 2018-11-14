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

## Pod template(YAML)

~~~~
apiVersion: v1
kind: Pod
metadata:
  name: myapp-pod
  labels:
    app: myapp
spec:
  containers:
  - name: myapp-container
    image: busybox
    imagePullPolicy: IfNotPresent
    command: ['sh', '-c', 'echo Hello Kubernetes! && sleep 3600']
    env:
    - name: III
      value: abc
    - name: UUU
      value: def
    volumeMounts:
    - mountPath: /mnt/abcd
      name: mnt-abcd
    - mountPath: /mnt/efgh
      name: mnt-efgh
    
    volumes:
    - name: mnt-abcd
      hostPath:
        path: /mnt/abcd
        type: Directory 
    - name: mnt-efgh
      hostPath:
        path: /mnt/efgh
        type: Directory 
~~~~

1. .spec.containers is a list all the containers that are part of the pod.
2. .spec.containers[0].image is the image name from which the container has to be created.
3. .spec.containers[0].imagePullPolicy is self explanatory. Takes following values: IfNotPresent, Always, Never.
4. .spec.containers[0].command is entrypoint to the container.
5. .spec.containers[0].env is a list of environment variables to be passed to the container.
6. .spec.containers[0].volumeMounts is a list of volumes to be mounted in the container.
7. .spec.volumes is the a list of volumes created which can be mounted in any of the pod containers using the above volumeMounts specifier.
