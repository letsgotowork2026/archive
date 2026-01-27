
# 사람의 수
N = int(input())

# 각 사람이 돈을 인출하는데 걸리는 시간
    # map 함수를 이용하면 for문을 쓰지 않고 한 줄에 여러개의 정수 입력 받을 수 있음
P_i = list(map(int, input().split()))

# 오름차순으로 정렬
P_i.sort()

time = []

for i in range(N):
    temp = 0
    for j in range(i + 1):
        temp += P_i[j]
    time.append(temp)

ans = sum(time)
print(ans)
