서비스가 생성되면, 파드가 어떤 노드에 있는지에 관계없이 클러스터의 모든 파드에서 액세스할 수 있습니다.

하지만 이 서비스는 클러스터 내에서만 액세스할 수 있다.

이러한 유형의 서비스를 클러스터 IP라고 한다.

Kubelet 서비스는 kube-api-server를 통해 클러스터 변경 사항을 감시한다.

CNI 플러그인을 호출하여 Pod에 대한 네트워킹을 구성한다.

각 노드 별로 kube-proxy는 kube-api-server를 통해 클러스터의 변경사항을 감시한다.

kube-api-server > kubelet > kube-proxy

# Service

서비스는 각 노드에 생성되거나 각 노드에 할당되는 구조가 아니다.

서비스는 클러스터의 전반 개념이다.

Pod < Container < Namespace, Service < IP

