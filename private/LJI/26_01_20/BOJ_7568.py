
N = int(input())

# 파이썬에서는 반복을 수행하되, 변수 값이 필요 없을 때 언더바(_)를 사용할 수 있음
arr = [list(map(int, input().split())) for _ in range(N)]

for i in arr:
    rank = 1
    for j in arr:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = ' ')
