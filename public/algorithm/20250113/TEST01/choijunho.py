import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
arr = []
vis = []

for i in range(N):
    arr.append(list(map(int, input().split())))
    vis.append([False for _ in range(N)])

queue = deque()
queue.append([0, 0])
while len(queue):
    x, y = queue.popleft()

    if vis[x][y]:
        continue
    vis[x][y] = True

    delta = [[arr[x][y], 0], [0, arr[x][y]]]
    for dx, dy in delta:
        tx = x + dx
        ty = y + dy
        if tx >= N or ty >= N:
            continue
        queue.append([tx, ty])

print("HaruHaru" if vis[N - 1][N - 1] else "Hing")