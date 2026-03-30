# network namespace

네트워크 환경 격리 기술

다음과 같은 네트워크 자원들이 독자적으로 할당

- 네트워크 인터페이스: (eth0, lo 등)
- 라우팅 테이블: (데이터가 어디로 갈지 경로 결정)
- IP 주소: (각 네임스페이스마다 같은 IP를 가질 수도 있음)
- 방화벽(iptables) 규칙
- 포트 번호: (A 네임스페이스의 80번 포트와 B 네임스페이스의 80번 포트는 별개)

`ip netns add <namespace-name>`

`arp`

`route`