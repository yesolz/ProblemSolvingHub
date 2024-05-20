from collections import deque
import sys
input = sys.stdin.readline

# 사용자 수 N, 친구 관계 수 M 입력
N, M = map(int, input().split())

# 그래프 초기화
graph = [[] for _ in range(N + 1)]

# 친구 관계 입력
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

# BFS 함수 정의
def bfs(start):
    distances = [-1] * (N + 1)
    queue = deque([start])
    distances[start] = 0
    
    while queue:
        current = queue.popleft()
        
        for neighbor in graph[current]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
    
    return distances

# 모든 사용자에 대해 케빈 베이컨 수 계산
min_bacon_number = sys.maxsize
result_person = -1

for i in range(1, N + 1):
    distances = bfs(i)
    bacon_number = sum(distances[1:])  # 1번 사용자부터 N번 사용자까지의 거리 합
    
    if bacon_number < min_bacon_number:
        min_bacon_number = bacon_number
        result_person = i

# 결과 출력
print(result_person)
