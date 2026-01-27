# Vertical Pod AutoScaler

포드 템플릿의 컨테이너 섹션 아래에서 배포에 할당된 리소스 요청과 제한을 변경한 다음 저장합니다. 그러면 해당 파드가 죽고 새 파드가 만들어집니다.

- Observe metrics
- Adds pod resources
- Balances thresholds


- VPA Admission Controller
- VPA Updater
- VPA Recommender

VPA Mode

`Off`

Only recommends; does not change anything

`Initial`

Only changes on Pod creation; not later

`Recreate`

Evicts pods if usage goes beyond range

`Auto`

Updates existing pods to recommended numbers - For now, it behaves like Recreate. But when support for "In-Place Update of Pod Resources" is available, this mode will be preferred

# VPA (Vertical Scaling)

## Scaling Method
Increases CPU and memory of existing Pods

## Pod Behavior
Restarts Pods to apply new resource values

## Handles Traffic Spikes?
No, because scaling requires a Pod restart 

## Optimizes Costs?
Prevents over-provisioning of CPU/memory

## Best for
Stateful workloads, CPU/memory-heavy apps (DBs, ML workloads)

## Example Use Cases
Databases (MySQL, PostgreSQL), JVM-based apps, Al/ML workloads

# HPA (Vertical Scaling)

## Scaling Method
Adds/Removes Pods based on load

## Pod Behavior
Keeps existing Pods running

## Handles Traffic Spikes?
Yes, instantly adds more Pods

## Optimizes Costs?
Avoids unnecessary idle Pods

## Best for
Web apps, microservices, stateless services

## Example Use Cases
Web servers (Nginx, API services), message queues, microservices