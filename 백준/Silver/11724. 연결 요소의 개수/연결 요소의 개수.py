import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N+1)

def dfs(v):
    stack = [v]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    stack.append(neighbor)

count = 0
for i in range(1, N+1):
    if visited[i] == False:
        count += 1
        dfs(i)
print(count)