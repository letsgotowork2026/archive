# Design Patterns

## Co-located Containers

이것이 멀티 컨테이너의 원래 형태입니다.

하나의 포드에서 두 개의 컨테이너를 실행하는 것만큼 간단합니다.

두 컨테이너는 전체 파드 수명 주기 동안 계속 실행되도록 되어 있습니다.

일반적으로 두 서비스가 서로 종속되어 있는 경우에 사용됩니다.

## Regular Init Containers

다음은 초기화 컨테이너 또는 요즘에는 초기화 컨테이너라고 부르는 컨테이너입니다.

이것은 메인 애플리케이션 자체보다 먼저 파드가 시작될 때 수행해야 하는 초기화 단계가 있을 때 사용됩니다.

예를 들어, 메인 애플리케이션을 시작하기 전에 데이터베이스가 준비될 때까지 기다리는 초기화 컨테이너가 될 수 있습니다.

초기화 컨테이너가 작업을 수행하고 작업을 종료하면 기본 애플리케이션이 시작됩니다.

```
apiVersion: v1
kind: Pod
metadata:
    name: simple-webapp
    labels:
        name: simple-webapp
spec:
    containers:
    - name: web-app
      image: web-app
      ports:
        - containerPort: 8080
    - name: main-app
      image: main-app
```

## Sidecar Containers

세 번째 유형은 사이드카 컨테이너로 알려져 있습니다.

사이드카 컨테이너는 초기화 컨테이너처럼 설정되어 사이드카가 먼저 시작하여 작업을 수행하지만

실행이 종료되는 대신 파드의 수명 주기 동안 계속 실행됩니다.

사이드카 컨테이너가 시작된 후 메인 애플리케이션이 시작됩니다.

이 기능은 주 앱이 시작되기 전에 시작해야 하지만 주 앱이 실행되는 동안 계속 실행되고 주 앱이 종료된 후 종료되어야 하는 로그 수집기와 함께 실행해야 하는 로그 수집기가 있는 경우에 유용합니다.

```
apiVersion: v1
kind: Pod
metadata:
    name: simple-webapp
    labels:
        name: simple-webapp
spec:
    containers:
    - name: web-app
      image: web-app
      ports:
        - containerPort: 8080
    initContainers:
    - name: main-app
      image: main-app
    - name: sub-app
      image: sub-app
```

## Co-located Containers vs Sidecar Containers

이 두 경우 모두 라이프사이클 내내 파드가 실행되고 있음을 알 수 있습니다.

따라서 가장 큰 차이점은 공동 배치된 컨테이너의 경우 어떤 컨테이너가 먼저 시작되는지, 그 시작 순서를 정의할 수 없다는 것입니다.

그러나 사이드카 컨테이너 옵션은 시작 순서를 지정한 다음 파드 수명 주기 동안 계속 실행할 수 있는 기능을 제공합니다.

```
apiVersion: v1
kind: Pod
metadata:
    name: simple-webapp
    labels:
        name: simple-webapp
spec:
    containers:
    - name: web-app
      image: web-app
      ports:
        - containerPort: 8080
    initContainers:
    - name: main-app
      image: main-app
      restartPolicy: Always
```
그러나 초기화 컨테이너는 항상 재시작 정책이 항상으로 설정되어 있으므로 계속 실행됩니다.

따라서 주 애플리케이션이 중지된 후에도 초기화 컨테이너가 종료되도록 합니다.