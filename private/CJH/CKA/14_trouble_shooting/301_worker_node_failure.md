# Node Status

`kubectl get nodes`

`kubectl describe node <node-name>`

node에 대한 Condition State를 확인할 수 있다.

문제에 대하여 True/False로 표현되는데, Crash로 인해 Master Node와 통신이 중단된다면 Known으로 설정된다.

# Node Capacity

`top` `df -h`

노드에서 가능한 CPU, 메모리 및 디스크 공간을 확인한다.

# Kubelet Status

`service kubelet status`

`sudo journalctl -u kubelet`

(journalctl: systemd 데몬이 수집하는 중앙 집중형 로그(저널)를 조회하고 필터링하는 강력한 커맨드라인 유틸리티)

`service kubelet status`
`service kubelet start`

# Certificates

`openssl x509 -in /var/lib/kubelet/<node-name>.crt -text`