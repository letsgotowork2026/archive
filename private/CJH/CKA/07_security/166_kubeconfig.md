```
apiVersion: v1
kind: Config

clusters:
- name: production
  cluser:
    certificate-authority: ca.crt
    server: <server-ip>

contexts:
- name: admin@production
  context:
    cluster: production
    user: admin
namespace: finance

users:
- name: admin
  user:
    client-certificate: admin.crt
    client-key: admin.key
```
