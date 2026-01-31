각 파드에 대해, 어떤 스토리지 솔루션을 사용하든, 파드를 배포하는 사용자는 자신의 환경에 있는 모든 파드 정의 파일에서 이를 구성해야 합니다.

변경을 할 때마다 사용자는 모든 포드에서 변경을 해야 합니다.

대신 스토리지를 보다 중앙에서 관리하고자 합니다.

영구 볼륨은 클러스터에 애플리케이션을 배포하는 사용자가 사용할 수 있도록 관리자가 구성한 클러스터 전체 스토리지 볼륨 풀입니다.


```
apiVersion: v1
kind: PersistentVolume
metadata:
    name: <persistent-volume-name>
spec:
    accessMode:
    - ReadWriteOnce
    capacity:
      storage: 1Gi
    hostPath
      path: /tmp/data
```

AccessMode
- ReadWriteOnce
- ReadOnlyMany
- ReadWriteMany