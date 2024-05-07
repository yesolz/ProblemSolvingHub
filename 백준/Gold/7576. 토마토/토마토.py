from collections import deque

m, n = map(int, input().split()) # 가로, 세로

graph = []
for i in range(n):
    x = list(map(int, input().split()))
    graph.append(x)

queue = deque()
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 초기에 익은 토마토 위치 큐에 삽입
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))

def bfs():
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

bfs()

max_days = 0
for row in graph:
    for value in row:
        if value == 0:
            print(-1)
            exit()
        max_days = max(max_days, value)

print(max_days - 1) # 처음 토마토 제외