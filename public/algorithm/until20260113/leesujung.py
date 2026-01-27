from collections import deque

n = int(input())
area = []

for i in range(n):
    area.append(list(map(int, input().split(' '))))

visited = [[False] * n for _ in range(n)]

queue = deque()
queue.append([0,0])

while len(queue):
    x, y = queue.popleft()

    if visited[x][y] == True:
        continue
    visited[x][y] = True

    delta = [[area[x][y], 0], [0, area[x][y]]]
    for dx, dy in delta:
        nx = x + dx
        ny = y + dy
        if nx >= n or ny >= n:
            continue
        queue.append([nx, ny])
    
    
print("HaruHaru" if visited[n-1][n-1] == True else "Hing")
