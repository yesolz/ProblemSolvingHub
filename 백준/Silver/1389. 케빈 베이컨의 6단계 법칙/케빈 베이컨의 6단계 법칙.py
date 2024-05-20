import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 거리 배열 초기화
INF = sys.maxsize
dist = [[INF] * (N+1) for _ in range(N+1)]

# 자신과의 거리는 0으로
for i in range(1, N+1):
    dist[i][i] = 0

# 친구 관계 입력
for _ in range(M):
    A, B = map(int, input().split())
    dist[A][B] = 1
    dist[B][A] = 1

# 플로이드-워셜
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

min_bacon_num = INF
result_person = -1

for i in range(1, N+1):
    bacon_num = sum(dist[i][1:])
    if bacon_num < min_bacon_num:
        min_bacon_num = bacon_num
        result_person = i

print(result_person)