# helm

kubernetes 패키지 관리자

1. 수많은 resource에 대한 yaml이 필요하다
2. 인터넷에서 받을 수 있는 yaml에 대해서 커스텀화를 개별로 해야한다.
3. 삭제할때 단일 yaml파일로 관리하기 번거롭다.

`helm install <app-name>`
`helm upgrade <app-name>`
`helm rollback <app-name>`
`helm uninstall <app-name>`