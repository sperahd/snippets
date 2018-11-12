## Overview

### Kubernetes Master Node processes:
1. kube-apiserver
2. kube-controller
3. kube-scheduler

### Kubernetes Worker Node processes:
1. kubelet - The process which communicates to the K8s master.
2. kube-proxy - A network proxy which reflects K8s networking services running on each node.

## K8s objects

K8s objects are persistent entities which define the state of the cluster. Following information is described using objects:
1. what containerized applications are running(and their nodes).
2. associated network and disk resources
3. Policies around these applications behavior(restart, fault-tolerance, etc.)

A Kubernetes object is a “record of intent”–once an object is created, the Kubernetes system will constantly work to ensure that object exists. By creating an object, you’re effectively telling the Kubernetes system what you want your cluster’s workload to look like; this is your cluster’s desired state. 

To work with K8s object we need to kubectl or the kubernetes api in a particular programming language of choice.

Each K8s object includes two top level object fields called spec and status.
1. Spec - It defines the desired state that you want your cluster to reach and it's associated characteristics
2. Status - It is actual state of the object and is provided(updated) by the K8s system. At any point the K8s control plane's job is to manage the cluster's actual state to match cluster's desired state.

Example on how K8s objects work to manage desired state to match actual state

&nbsp;&nbsp;&nbsp; A k8s deployment is an object that can represent an application running on the cluster. When a deployment(3 replicas of a container) is created with a defined spec, K8s system reads the deployment spec and tries to run 3 instances of the container specified. If all the 3 containers run as expected the status is matching the spec as soon as one replica dies the K8s system responds to this by trying to replace the dead container with a new container so that the number of running instances match the spec defined.

## How to define K8s objects?

K8s objects are defined using a yaml description which can then be used by kubectl to create the service. 

Example YAML:

~~~~
apiVersion: apps/v1 # for versions before 1.9.0 use apps/v1beta2
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  selector:
    matchLabels:
      app: nginx
  replicas: 2 # tells deployment to run 2 pods matching the template
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.7.9
        ports:
        - containerPort: 80
~~~~
