from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def bfs(grid, n, m):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    distance = [[-1] * m for _ in range(n)]
    queue = deque()

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                queue.append((i, j))
                distance[i][j] = 0
            elif grid[i][j] == 0:
                distance[i][j] = 0

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == 1 and distance[nx][ny] == -1:
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))

    return distance

distances = bfs(grid, n, m)
for row in distances:
    print(' '.join(map(str, row)))