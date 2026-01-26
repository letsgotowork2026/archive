# CSI Driver

```
apiVersion: secrets-store.csi.x-k8s.io/v1
kind: SecretProviderClass
metadata:
    name: db-secrets
spec:
    provider: aws
    parameters:
        objects: |
            - objectName: "db-creds"
              objectType: "secretsmanager"
```

```
spec:
    volumes:
    - name: db-creds
      csi:
        driver: secrets-store.csi.k8s.io
        readOnly: true
        volumeAttributes:
            secretProviderClass: db-secrets
    cotainers:
    - name: <container-name>
      image: <image-name>
      volumeMounts:
        - name: db-creds
          mountPath: /tmp
```