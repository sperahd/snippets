## Pods

### To list all the running pods

~~~~
kubectl get pod
~~~~

### To check status of a pod

~~~~
kubectl describe pod $pod_name
~~~~

### To delete a kubectl pod

~~~~
kubectl delete pod $pod_name
~~~~

## configMaps

### To list all the configMaps

~~~~
kubectl get configMaps
~~~~

## Deployment Controller

### To start a deployment controller

~~~~
kubectl apply -f $file_name_yaml
~~~~

### To list deployments

~~~~
kubectl get deployment
~~~~

### To delete a deployment controllerr

~~~~
kubectl delete deployment $deployment_name
~~~~

## Service (Nodeport, etc.)

### To list all the services (services in container world is anything that exposes ports)

~~~~
kubectl get service
~~~~

### To describe a particular service

~~~~
kubectl describe service $service_name
~~~~
