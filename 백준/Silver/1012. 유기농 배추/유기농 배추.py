def dfs(x, y, graph, visited, n, m):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    stack = [(x, y)]
    visited[y][x] = True

    while stack:
        cur_x, cur_y = stack.pop()
        for dx, dy in directions:
            nx, ny = cur_x + dx, cur_y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and graph[ny][nx] == 1:
                visited[ny][nx] = True
                stack.append((nx, ny))


def count(n, m, cabbages):
    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    for x, y in cabbages:
        graph[y][x] = 1

    count = 0
    for y in range(n):
        for x in range(m):
            if graph[y][x] == 1 and not visited[y][x]:
                dfs(x, y, graph, visited, n, m)
                count += 1

    return count


t = int(input())
results = []
for _ in range(t):
    m, n, k = map(int, input().split())
    cabbages = [tuple(map(int, input().split())) for _ in range(k)]
    results.append(count(n, m, cabbages))

for r in results:
    print(r)