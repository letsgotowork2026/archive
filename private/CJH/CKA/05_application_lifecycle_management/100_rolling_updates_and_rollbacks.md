# Rollout Command

`kubectl roolout status deployments/deployment-name`

`kubectl roolout history deployments/deployment-name`

# Deployment Strategy

`kubectl describe deployment deployment-name`

## Recreate

v1 모두 다운 후 v2 모두 업
  
## Rolling Update

v1 일부 다운 후 v2 일부 업
v1 나머지 다운 후 v2 나머지 업

# Rollback after Upgrades


## Upgrades

ReplicaSet-1 삭제됨과 동시에 ReplicaSet-1 생성

`kubectl get replicasets`

v1 0 pods
v2 N pods

## Rollback

`kubectl rollout undo deployment deployment-name`

v1 N pods
v2 0 pods

# Commands Summary

## Create

`kubectl create -f deployment-definition.yaml`

## Get

`kubectl get deployments`

## Update

`kubectl apply -f deployment-definition.yaml`
`kubectl set image deployment/deployment-name <컨테이너명>=<이미지명:태그>`

## Status

`kubectl rollout status deployment/deployment-name`
`kubectl rollout history deployment/deployment-name`

## Rollback

`kubectl rollout undo deployment/deployment-name`