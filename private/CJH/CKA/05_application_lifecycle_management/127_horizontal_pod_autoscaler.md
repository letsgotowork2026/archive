# Horizontal Pod Autoscaler

```
apiVersion: apps/v1
kind: Deployment
metadata:
    name: my-app
spec:
    replicas: 1
    selector:
        matchLabels:
            app: my-app
    template:
        metadata:
            labels:
                app: my-app
        spec:
            containers:
            - name: my-app
              image: nginx
              resources:
                requests:
                    cpu: "250m"
                limits:
                    cpu: "500m"
```

```
kubectl autoscale deployment my-app --cpu-percent=50 --min=1 --max=10
```

```
kubectl get hpa
```