# Dynamic Programming 

## 중복 연산을 줄이자
<컴퓨터: 연산속도 제한, 메모리 공간 한정적> => 연산 속도, 메모리 공간 최대한 활용하는 효율적 알고리즘 작성

동적 할당의 `Dynamic` = 프로그램이 실행되는 도중에

## DP 사용 가능한 조건
1. 큰 문제를 작은 문제로 나눌 수 있다
2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다

- 일단 재귀함수로 비효율적으로 작성한 후 메모이제이션 적용 가능 여부를 따져보기

### Memoization
DP 구현 Top Down에서 국한되어 사용
- 한번 구한 결과를 메모리 공간에 메모해두고 같은 식을 다시 호출하면 메모한 결과를 그대로 가져옴
== `Caching`

- 한번 계산한 데이터를 리스트에 저장
  - 딕셔너리 사용할수도 (연속적이지 않은 경우)
- 피보나치 수열 계산) DP 사용시 O(n)을 가짐 
  - 원래는 O(2^n) 2의 n승 시간복잡도

## 2가지 방식
웬만하면 바텀업으로 풀자
recursion depth 오류 발생 가능 
    - sys의 setrecursionlimit()으로 완화 가능
### 탑다운 Top Down
- 큰 문제 해결을 위해 작은 문제를 호출
- 메모이제이션은 탑다운에 국한
- 하향식

```python
d = [0] * 100

def pibo(n):
    print('f('+str(n)+')')
    if (n == 1 or n == 2):
        return 1
    if d[n] != 0:
        return d[n]
    d[n] = pibo(n-1) + pibo(n-2)
    return d[n]

pibo(6)
```
### 바텀업 Bottom Up
- for문으로 아래에서 위로 올라가는 형식
- 전형적인 풀이 방식
- 상향식
```python
d = [0]*100 # DP table

d[1] = 1
d[2] = 1
n = 6

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])
```

