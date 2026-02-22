# dns

domain name system

사람이 이해하기 쉬운 도메인 이름

# kube dns
- node1.kubecluster.org
  192.168.1.11
- node2.kubecluster.org
  192.168.1.12
- node3.kubecluster.org
  192.168.1.13

# Service Record

kube dns
아래 IP 매핑 테이블을 갖고 있게 된다

hostname: web-service
ip address: 10.107.37.188

test (pod,10.244.1.5) > web-service (service, 10.107.37.188) > web (pod, 10.244.2.5)

`curl http://web-service`

만약 namespace가 다르다면, web이 apps라는 namespace에 존재한다.

`curl http://web-service.apps`

hostname < namespace < type (ex. svc) > root (cluster.local) < ip address

`curl http://web-service.apps.svc.cluster.local`
