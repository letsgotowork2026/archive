values.yaml
```
replicaCount: 1

image:
    repository: nginx
```

Chart.yaml
```
apiVersion: v2
appVersion: "1.16.0"
name: hello-world
description: A web application

type: application
```

`v1=helm version 2`
`v2=helm version 3`
