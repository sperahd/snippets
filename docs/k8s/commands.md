## minikube

### To copy a file from local system to minikube env

~~~~
scp -i $(minikube ssh-key) $local_file docker@$(minikube ip):$path_to_copy_to
~~~~

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

### To create a configmap from a file

Note1: Following will create a configMap from a file abcd.json as config.json
Note2: A configMap mapped file cannot be edited
~~~~
kubectl create configmap config-json --from-file=config.json=abcd.json
~~~~

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

### To send udp data from host system to container running in minikube vm

Following creates a service
~~~~
kubectl expose deployment $dep_name --port=$Portrequired --type=NodePort --protocol=UDP --name=$dep-name-udp-in
kubectl get service $dep-name-udp-in
~~~~

Output
~~~~
$dep-name-udp-in   NodePort   10.103.121.154   <none>        $actual_port:$mapped_port/UDP   2h
~~~~

Check minikube ip

~~~~
minikube ip
~~~~

Figure out minikube ip interface(generally it is vboxnet0)

To stream udp to the container using above NodePort
~~~~
./udp_send.sh <interface> <minikube-ip> <$mapped_port>
~~~~

### To send udp data from minikube container to host system

Stream to the local ip of the host system
