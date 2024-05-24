from collections import deque

import sys
input = sys.stdin.readline

def bfs(x, y, graph, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    count = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if graph[nx][ny] == 'P':
                    count += 1
                if graph[nx][ny] in ['P', 'O']:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    return count

N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

count = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'I':
            count = bfs(i, j, graph, visited)

if count > 0:
    print(count)
else:
    print("TT")