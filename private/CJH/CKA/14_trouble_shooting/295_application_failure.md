# Checking Accessibility

User < Web Service < Web Pod < DB Service < DB Pod

`curl http://web-service-ip:node-port`

`kubectl describe service web-service`

1. check service endpoint
2. check pod selector (label)

`kubectl get pod`
`kubectl describe pod web`
`kubectl logs web`, `kubectl logs web -f --previous`

1. 파드 상태 확인
2. 파드 로그 확인
