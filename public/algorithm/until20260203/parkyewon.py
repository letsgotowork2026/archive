T = int(input())

for i in range(T):
    answer = 1
    N, M = map(int, input().split())

    for j in range(2, M + 1):
        answer *= j

    for j in range(2, N + 1):
        answer //= j

    for j in range(2, M - N + 1):
        answer //= j

    print(int(answer))

