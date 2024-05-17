import sys

input = sys.stdin.readline


def floyd_warshall(n, graph):
    reach = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                reach[i][j] = 1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if reach[i][k] and reach[k][j]:
                    reach[i][j] = 1

    return reach


n = int(input().strip())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().strip().split())))

result = floyd_warshall(n, graph)

for row in result:
    print(" ".join(map(str, row)))