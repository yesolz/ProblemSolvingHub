n, m, v = map(int, input().split())

# 그래프 - 노드 연결 정보 (2차원 리스트)
graph = [[0] * (n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

# 방문 정보
visited1 = [False] * (n+1)
visited2 = visited1.copy()

def dfs(v):
    visited1[v] = True
    print(v, end=' ')
    for i in range(1, n+1):
        if graph[v][i] == 1 and visited1[i] == False:
            dfs(i)

def bfs(v):
    queue = [v]
    visited2[v] = True
    while queue:
        v = queue.pop(0)
        print(v, end=' ')
        for i in range(1, n+1):
            if graph[v][i] == 1 and visited2[i] == False:
                queue.append(i)
                visited2[i] = True

dfs(v)
print()
bfs(v)