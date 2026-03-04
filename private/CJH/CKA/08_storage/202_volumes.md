컨테이너에서 처리된 데이터를 유지하기 위해 컨테이너에 볼륨을 첨부합니다.

생성할 때 이제 컨테이너에서 처리된 데이터는 이 볼륨에 저장되어 영구적으로 유지됩니다.

컨테이너가 삭제되더라도 컨테이너에서 생성되거나 처리된 데이터는 그대로 남아 있습니다.

```
apiVersion: v1
kind: Pod
metadata:
    name: random-number-generator
spec:
    containers:
    - image: alpine
      name: alpine
      command: ["/bin/sh", "-c"]
      args: ["shuf -i 0-100 -n 1 >> opt/number.out;"]
      volumeMounts:
      - mouthPath: /opt
        name: data-volume
    volumes:
    - name: data-volume
    hostPath:
      path: /data
      type: Directory
```

```
volumes:
- name: data-volume
  awsElasticBlockStore:
    volumeID: <volume-id>
    fsType: ext4
```