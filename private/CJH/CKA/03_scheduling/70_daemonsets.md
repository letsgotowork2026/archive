# 70. DaemonSets

- Daemonset은 Replicaset과 유사
- 여러 개의 Pod Instance를 배포하는 데 도움
- Cluster의 각 노드에서 하나의 Pod 사본을 실행
- 각 Node에서 하나의 Pod 사본을 실행
- Cluste에 새 Node가 추가될 때마다 해당 Node에 Pod의 복제본이 자동으로 추가
- 노드가 제거되면 Pod도 자동으로 제거
- Daemonset은 Cluster의 모든 Node에 항상 하나의 Pod 사본이 존재하도록 함

## Daemonset Usecase

> Monitoring

>> 클러스터의 각 노드에 모니터링 에이전트 또는 로그 수집기를 배포하여 클러스터를 자동으로 모니터링 싶을 때

데몬 세트는 클러스터의 모든 노드에 포드 형태로 모니터링 에이전트를 배포 가능

> kube-proxy

워커 노드 구성 요소 중 하나가 kube-proxy

kube 프록시 구성 요소는 클러스터에 데몬셋으로 배포 가능

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: monitoring-daemon
spec :
  selector:
    matchLabels:
      app: monitoring-agent
  template:
    metadata:
      labels:
        app: monitoring-agent
    spec :
      containers:
      - name: monitoring-agent
        image: monitoring-agent
```
