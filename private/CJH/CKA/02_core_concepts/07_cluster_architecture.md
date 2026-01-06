# 7. Cluster Architecture

01 Kubernetes Architecture
02 etcd for Beginners
03 etcd in Kubernetes
04 Kube-API Server
05 Controller Managers
06 Kube Scheduler
07 Kubelet
08 Kube Proxy

## Kubernets Architecture

Kubernetes 클러스터는 컨테이너 형태로 애플리케이션을 호스팅하는 물리적 또는 가상, 온프레미스 또는 클라우드에 있는 노드 집합으로 구성

> Worker Nodes

> Master Node

쿠버네티스 클러스터를 관리하고, 여러 노드에 관한 정보를 저장하고, 어떤 컨테이너가 어디로 이동할지 계획하고, 노드와 컨테이너를 모니터링하는 등의 작업을 담당

컨트롤 플레인 컴포넌트라고 하는 일련의 컴포넌트를 사용하여 이 모든 작업을 수행

> etcd Cluster

정보를 키 값 형식으로 저장하는 데이터베이스


> Kube-Scheduler

컨테이너 리소스 요구 사항, 워커 노드 용량 또는 테인트 및 허용 오차 또는 노드 선호도 규칙과 같은 기타 정책이나 제약 조건에 따라 컨테이너를 배치할 올바른 노드를 식별

> Controller-Manager

>> Node-Controller

클러스터에 새 노드를 온보딩하고, 노드를 사용할 수 없게 되거나 파괴되는 상황을 처리하며 노드를 관리

>> Replication-Controller

복제 컨트롤러는 복제 그룹에서 원하는 수의 컨테이너가 항상 실행되도록 보장

>> Controller-Manager

> Kube-apierver

kube-apiserver
- Kube-Scheduler
- etcd Cluster
- Controller-Manager
- ...

클러스터 내의 모든 작업을 오케스트레이션하는 역할을 담당

클러스터에서 관리 작업을 수행하는 데 사용되는 Kubernetes API와 클러스터의 상태를 모니터링하고 워커 노드가 서버와 통신하는 데 필요한 변경을 수행하는 다양한 컨트롤러를 노출

> Container Runtime Engine

Docker
(+ containerd, rkt)

> Kubelet

클러스터의 각 노드에서 실행되는 에이전트

Kube-apiserver의 지시를 수신하고 필요에 따라 노드에 컨테이너를 배포하거나 삭제

Kube-apiserver는 주기적으로 Kubelet에서 상태 보고서를 가져와 노드와 그 위에 있는 컨테이너의 상태를 모니터링


> Kube-proxy

워커 노드 간의 통신은 워커 노드에서 실행되는 또 다른 구성 요소인 Kube-proxy에 의해 활성화

워커 노드에서 실행 중인 컨테이너가 서로 연결될 수 있도록 필요한 규칙이 워커 노드에 적용되도록 지원