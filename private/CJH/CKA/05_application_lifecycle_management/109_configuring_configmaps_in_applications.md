# ConfigMap

1. create configmap
2. inject into pod

## imperative

`kubectl create configmap <config-name> --from-literal=<key>=<value>`

```
kubectl create configmap <config-name> \
    --from-literal=<key1>=<value1> \
    --from-literal=<key2>=<value2>
```

```
kubectl create configmap <config-name> \
    --from-file=<path-file> \
```

## declarative

`kubectl create -f <config-file-name>`

```
apiVersion: v1
kind: ConfigMap
metadata:
    name: <config-name>
data:
    <key1>: <value1>
    <key2>: <value2>
```


# ConfigMap in Pods

## Env

```
apiVersion: v1
kind: Pod
metadata:
    name: <pod-name>
spec:
    containers:
    - name: <container-name>
      image: <image-name>
      ports:
      - containerPort: <port>
      envFrom:
      - configMapRef:
        name: <config-name>
```

## Single Env
```
apiVersion: v1
kind: Pod
metadata:
    name: <pod-name>
spec:
    containers:
    - name: <container-name>
      image: <image-name>
      ports:
      - containerPort: <port>
      envFrom:
      - configMapRef:
        name: <config-name>
        key: <env-key>
```

## Volume


```
apiVersion: v1
kind: Pod
metadata:
    name: <pod-name>
spec:
    containers:
    - name: <container-name>
      image: <image-name>
      ports:
      - containerPort: <port>
    volumes
    - name: <volume-name>
      configMap:
        name: <config-name>
```