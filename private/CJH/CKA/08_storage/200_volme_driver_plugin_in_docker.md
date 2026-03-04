storage drivers

- aufs
- zfs
- btrfs
- device mapper
- overlay
- overlay2

volume drivers

- local
- azure file storage
- convoy
- digitalocean block storage
- flocker
- gce-docker
- GlusterFS
- NetApp
- Rexray
- portworx
- wmware vsphere storage

```
docker run -it \
    --name mysql
    --volume-driver rexray/ebs
    --mount src=ebs-vol, target=/var/lib/mysql
    mysql
```