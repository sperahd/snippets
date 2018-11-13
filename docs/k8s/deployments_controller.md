## Deployment Controller YAML template

~~~~
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.15.4
        ports:
        - containerPort: 80
~~~~

1. .spec.kind specifies that the object controller to be used is deployment.
2. .spec.etadata specifies the uniquely identifiable name and labels of the deployment.
3. .spec section specifies the desired state of the deployment to be reached.
4. .spec.template is a pod template and has exactly same schema as a single pod.
5. .spec.replicas is an optional field, it defaults to 1.
6. .spec.selector must match .spec.template.metadata.labels, or it will be rejected by the API
