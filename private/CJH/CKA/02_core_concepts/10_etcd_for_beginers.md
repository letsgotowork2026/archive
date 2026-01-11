# 10. ETCD For Beginners

## Relational Database vs Documnet Store vs Key-Value Store

### Document Store

서로 영향을 주지않는 데이터 형태

```
{
    "name": "John Doe",
    "age": 45,
    "locaiton": "New York",
    "salary": 5000
}
```
```
{
    "name": "Lauren Rob",
    "age": 13,
    "locaiton": "Bangalore",
    "Grade": "C"
    "organization": "ACME"
}
```

### Key-Value Store

키 값 저장소에는 스키마가 반드시 필요하지 않으며 복잡한 쿼리를 지원하지 않음

하지만 성능이 매우 빠르고 유연성이 뛰어나 다른 것을 손상시키거나 데이터 구조에 대한 걱정없이 거의 모든 것을 저장할 수 있으므로 간단한 빠른 조회에 가장 적합

```
Key: location
Value: New York
```
```
Key: user: john_doe
Value: name=John Doe, age=45, location=New York, salary=5000
```

## ETCD 실행

etcd server 실행

```
    $ ./etcd
```

etcd client 실행

```
    $ ./etcd put key1 value1
```
```
    $ ./etcd get key1
    value1
```