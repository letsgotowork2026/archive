# VIM

## VIM 이동
Ctrl + f: 한 페이지 아래로 이동 (Forward)
Ctrl + d: 반 페이지 아래로 이동 (Down)
Ctrl + b: 한 페이지 위로 이동 (Backward)
Ctrl + u: 반 페이지 위로 이동 (Up)

# VIM 검색
/검색어 커서 기준 아래방향 검색
?검색어 커서 기준 윗방향 검색
n 검색한 방향으로 이동
N 검색한 반대방향으로 이동

대소문자 구분 O `grep -I <찾은 단어>`
대소문자 구분 X `grep -i <찾은 단어>`

# Kubectl

`kubectl edit <리소스타입> <리소스명>`

`kubectl edit pod <pod-name>`
생성된 pod 수정에 대해서는 spec내의 극히 제한된 필드만 수정가능
- (1안) deployment,statefulset,daemonset을 수정한다
- (2안 - 1) `kubectl get pod <pod-name> -o yaml > <yaml-name>.yaml`
- (2안 - 2) `kubectl replace --force -f <yaml-name>.yaml`


`kubectl get <리소스타입> <리소스명> -n default -o yaml > <리소스 파일>.yaml`

`kubectl config set-context --current--namespace=<원하는_네임스페이스_이름>`