Ingress는 호스트일치, 경로일치와 같은 http 기반 규칙만 가능

tcp, udp, 트래픽 분할, 헤더 조작, 인증, 속도 제한 등은 현재 지원되지 않습니다.

Ingress에서의 annotation으로 관리하게 된다.

그리고 이러한 구성은 이제 이러한 특정 컨트롤러에서만 사용할 수 있습니다.

# Gateway API

게이트웨이 API는 레이어 4 및 레이어 7 라우팅에 중점을 둔 공식 Kubernetes 프로젝트입니다.

- Ingress
- LoadBalancing
- Service Mesh API

Gateway Class, Gateway, HttpRoute