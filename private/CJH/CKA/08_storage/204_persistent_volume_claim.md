퍼시스턴트 볼륨과 퍼시스턴트 볼륨 클레임은 쿠버네티스 네임스페이스에서 서로 다른 두 개의 오브젝트이다.

관리자는 영구 볼륨 세트를 생성하고 사용자는 영구 볼륨 클레임을 생성하여 스토리지를 사용합니다.

퍼시스턴트 볼륨 클레임이 생성되면, 쿠버네티스는 볼륨에 설정된 요청 및 속성을 기반으로 퍼시스턴트 볼륨을 클레임에 바인딩한다.

- sufficient capacity
- access mode
- volume mode
- storage class
- selector


사용 가능한 볼륨이 없는 경우, 클러스터에 새로운 볼륨이 제공될 때까지 영구 볼륨 클레임은 보류 중인 상태로 유지됩니다.

```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
    name: <persistent-volume-claim-name>
spec:
    accessMode:
    - ReadWriteOnce
    resources:
      requests:
        storage: 500Mi
```

Reclaim Policy

`persistentVolumeClaimPolicy`
1. Retain
Keeps PV and it's data
2. Delete
Delete PV
3. Recycle (deprecated)
Data is scrubbed and PV is made available for claims again