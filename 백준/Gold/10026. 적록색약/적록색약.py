from collections import deque

import sys
input = sys.stdin.readline

def bfs(grid, visited, start_x, start_y, n):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True
    color = grid[start_x][start_y]

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == color:
                visited[nx][ny] = True
                queue.append((nx, ny))

def count_regions(grid, n):
    visited = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(grid, visited, i, j, n)
                count += 1
    return count

def solve(n, grid):
    normal_grid = [list(row) for row in grid]
    color_blind_grid = [row.replace('G', 'R') for row in grid]
    color_blind_grid = [list(row) for row in color_blind_grid]

    normal_count = count_regions(normal_grid, n)
    color_blind_count = count_regions(color_blind_grid, n)

    return normal_count, color_blind_count

n = int(input())
grid = [input().strip() for _ in range(n)]

normal_count, color_blind_count = solve(n, grid)
print(normal_count, color_blind_count)