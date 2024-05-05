n = int(input())

graph = [list(map(int, input())) for _ in range(n)]
visited = [[False] * (n) for _ in range(n)]

def dfs(x, y):
    visited[x][y] = True
    count = 1
    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1 and visited[nx][ny] == False:
            count += dfs(nx, ny)
    return count

total = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == False:
            count = dfs(i, j)
            total.append(count)

print(len(total))
for c in sorted(total):
    print(c)
