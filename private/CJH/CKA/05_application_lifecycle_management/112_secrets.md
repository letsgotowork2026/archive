# Secret

## Imperative

```
kubectl create secret generic <secret-name> \
    --from-literal=<key1>=<value1> \
    --from-literal=<key2>=<value2> \
    --from-literal=<key3>=<value3>
```

```

kubectl create secret generic <secret-name> \
    --from-file=<path-file>
```

## Declarative

`kubectl create -f <secret-yaml>.yaml`

```
apiVersion: v1
kind: Secret
metadata:
    name: <secret-name>
data:
    <key1>: <value1>
    <key2>: <value2>
```


# Encoding Secrets

`echo -n <value> | base64`

(-n 자동 개행 생략)

# Decoding Secrets

`echo -n <value> | base64 --decode`

# Secrets in Pods

## env

```
apiVersion: v1
kind: Pod
metadata:
    name: <pod-name>
spec:
    containers
    - name: <container-name>
      image: <image-name>
      ports:
        - containerPort: <port>
      envFrom:
        - secretRef:
            name: <secret-name>
```

## volume

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
      secret:
        secretName: <secret-name>
```