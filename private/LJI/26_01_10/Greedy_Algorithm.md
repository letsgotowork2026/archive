## 📌 Greedy 알고리즘이란
#### ✨ 정의
: 미래를 고려하지 않고 오직 현재 시점에 가장 좋은 선택

---

## 📌 Greedy 알고리즘의 특징
#### ✨ 미래의 선택을 고려하지 않고 현재에만 충실한 것이 최적의 해가 될 수 있을까?
: 최적의 해를 항상보장하지는 못 함 
: 현재의 최적 해 != 전체의 최적 해

  코테 특성 상 항상 최적해 찾아야 하므로 최적해가 보장되는 조건에서만 그리디 알고리즘 사용

#### ✨ 최적해가 보장되는 조건
1) 현재의 선택이 미래의 선택에 영향을 주지 않는다
--> 탐욕스런 선택 조건 (Greedy Choice Property)

- 예시
![](https://velog.velcdn.com/images/jung_inny/post/52ef6724-30b2-464f-8ff2-cf2c1b357e20/image.png)

2) 부분의 최적 해가 모이면 전체의 최적 해가 된다
--> 최적 부분 구조 조건 (Optimal Substructure)

---

## 📌 Greedy 전략
#### ✨ 문제 풀이 핵심은 '정렬'
- 어떻게 정렬해야 위의 두 가지 조건을 만족할까

#### ✨ 그리디 알고리즘이 사용되는 예시
- AI에 있어서 결정 트리 학습법 (Decision Tree Learning)
- 활동 선택 문제 (Activity selection problem)
- 거스름돈 문제
- 최소 신장 트리 (Minimum spanning tree)
- 다익스트라 알고리즘
- 허프만 코드
- UNION&FIND 알고리즘

---

## 📌 Greedy 사용 이유
- DP 보다 더 빠름
- 완전 탐색이 가장 단순 무식하게 정답을 찾는 방식 / 너무 느림
- 이를 개선하기 위해 다이나믹 프로그래밍이라는 알고리즘 사용 / 항상 최적 해를 보장하기 위해 모든 경우의 수 고려해 느려짐

---

## 📌 추천 문제

![](https://velog.velcdn.com/images/jung_inny/post/89196b83-bbbe-423c-bdc4-26b729a4e65e/image.png)
