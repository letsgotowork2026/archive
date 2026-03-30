## DNS
www.test.com

※ 모든 Service 마다 Proxy-Server를 둘 수 없다.
※ 이것 또한 쿠버네티스 내부에서 관리하고 싶다.
※ Ingress가 없다면 Nginx과 같은 로드벨런싱 솔루션을 이용해야 한다.
## Ingress
= 단일 URL로 접근 가능하다.
= 보안 SSL도 구성 가능하다.
= 클러스터에 내장된 Layer 7 로드벨런서

## Service (Port)
App-Service, Streaming Service

## Pod
App-Pod, Streaming-Pod

## Service (Port)
DB-Service

## Pod
DB-Pod

Ingress Resources, Ingress Controller
