n = int(input()) # 컴퓨터의 수 (1~100 정수)
m = int(input()) # 직접 연결되어있는 컴퓨터 쌍의 수

graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)

def dfs(graph, start, visited):
    visited[start] = True
    count = 1

    for neighbor in graph[start]:
        if not visited[neighbor]:
            count += dfs(graph, neighbor, visited)

    return count

result = dfs(graph, 1, visited)

print(result - 1)