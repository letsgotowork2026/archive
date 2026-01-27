# Plain Key Value
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
    env:
    - name: <env-name>
      value: <env-value>
```

# ConfigMap
```
env:
- name: <env-name>
  valueFrom:
    configMapKeyRef:
```

# Secrets
```
env:
- name: <env-name>
  valueFrom:
    secretKeyRef:
```
