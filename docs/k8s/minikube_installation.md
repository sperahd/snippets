# K8s minikube environment setup on centos 7

## Virtualbox installation (5.2)

1. Import oracle's public key 

~~~~
$ wget https://www.virtualbox.org/download/oracle_vbox.asc; sudo rpm --import oracle_vbox.asc
~~~~

2. Download virtualbox repo file

~~~~
$ sudo  wget http://download.virtualbox.org/virtualbox/rpm/el/virtualbox.repo -O /etc/yum.repos.d/virtualbox.repo
~~~~

3. Install VirtualBox by enabling the virtualbox repo

~~~~
$ sudo yum --enablerepo=virtualbox install VirtualBox-5.2
~~~~

4. Confirm Installation by running

~~~~
$ sudo systemctl status vboxdrv
~~~~

## kubectl installation (1.12)

### Note: Preferably follow steps [here](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

1. Download kubernetes repo file

~~~~
cat <<EOF > /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
EOF
~~~~

2. Install kubectl

~~~~
$ yum install kubectl
~~~~

## minikube installation (v0.30.0)

### Note: Preferably follow steps [here](https://github.com/kubernetes/minikube/releases)

1. Download minikube binary

~~~~
$ curl -Lo minikube https://storage.googleapis.com/minikube/releases/v0.30.0/minikube-linux-amd64 && chmod +x minikube && sudo cp minikube /usr/local/bin/ && rm minikube
~~~~

## minikube usage and getting started (v0.30.0)

### Note: Preferably follow steps [here](https://kubernetes-cn.github.io/docs/getting-started-guides/minikube/#quickstart)

1. Start minikube based cluster

~~~~
$ minikube start --vm-driver=none
~~~~

2. Specifying parameters to minikube start(For more such parameters, check [here](https://darkowlzz.github.io/post/minikube-config/)

> Note: If there is already a minikube cluster, first delete it using:

~~~~
$ minikube stop; minikube delete
~~~~

~~~~
$ minikube start --memory 2048 --cpus 10
~~~~
> Note 0: If minikube delete is run without running minikube stop, minikube start fails next time onwards and the solution is to delete ~/.minikube/ directory

~~~~
$ sudo rm -rf ~/.minikube/
~~~~

> Note 1: Any new parameter cannot be applied after minikube start, minikube has to be first stopped and then deleted for any parameter addition.

> Note 2: If the above command is stuck at any point for more than 2-3 minutes there is good chance there is something wrong. Please check minikube logs by running:

~~~~
$ minikube logs
~~~~

3. Test minikube installation 

~~~~
$ kubectl run hello-minikube --image=k8s.gcr.io/echoserver:1.10 --port=8080
deployment.apps/hello-minikube created

$ kubectl expose deployment hello-minikube --type=NodePort
service/hello-minikube exposed

$ kubectl get pod; sleep 60; kubectl get pod
NAME                              READY     STATUS              RESTARTS   AGE
hello-minikube-3383150820-vctvh   0/1       ContainerCreating   0          3s
NAME                              READY     STATUS    RESTARTS   AGE
hello-minikube-3383150820-vctvh   1/1       Running   0          13s

$ curl $(minikube service hello-minikube --url)

Hostname: hello-minikube-7c77b68cff-8wdzq

Pod Information:
	-no pod information available-

Server values:
	server_version=nginx: 1.13.3 - lua: 10008

Request Information:
	client_address=172.17.0.1
	method=GET
	real path=/
	query=
	request_version=1.1
	request_scheme=http
	request_uri=http://192.168.99.100:8080/

Request Headers:
	accept=*/*
	host=192.168.99.100:30674
	user-agent=curl/7.47.0

Request Body:
	-no body in request-

$ kubectl delete services hello-minikube

$ kubectl delete deployment hello-minikube

~~~~

4. Stop minikube

~~~~
minikube stop
~~~~

5. Development efficiency with minikube

> k8s requires docker images to be stored in some docker registry from where the images can be pulled and run. In case of local dev setup, the steps might be too cumbersome and time consuming. minikube allows us to expose the host docker environment to minikube environment by running:

~~~~
$ eval $(minikube docker-env)
~~~~
