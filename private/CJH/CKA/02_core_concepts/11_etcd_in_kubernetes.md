# 11. ETCD in Kubernetes

- Node
- Pods
- Configs
- Secrets
- Accounts
- Roles
- Bindings
- Others

kubectl get 명령을 실행할 때 표시되는 모든 정보는 etcd 서버에서 가져온 것

1. ETCD 직접 설치

마스터 노드에서 직접 etcd를 서비스로 구성하여 etcd를 배포

2. ETCD Kubeadm

kubeadm은 etcd 서버를 kube 시스템 네임스페이스에 파드로 배포