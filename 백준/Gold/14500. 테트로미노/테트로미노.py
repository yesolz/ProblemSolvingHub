import sys
input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

# 최댓값 저장
result = 0

# ㅜ 모양 제외, dfs를 사용한 테트로미노 탐색
def dfs(x, y, depth, total):
    global result
    if depth == 4:  # 테트로미노 완성
        result = max(result, total)
        return
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, total + graph[nx][ny])
            visited[nx][ny] = False

# ㅜ 모양 예외 처리
def exce(x, y):
    global result
    shapes = [
        [(0, 0), (0, 1), (0, 2), (1, 1)],  # ㅜ
        [(0, 0), (1, 0), (2, 0), (1, 1)],  # ㅏ
        [(1, 0), (1, 1), (1, 2), (0, 1)],  # ㅗ
        [(0, 1), (1, 0), (1, 1), (2, 1)]   # ㅓ
    ]
    for shape in shapes:
        try:
            temp_sum = 0
            for dx, dy in shape:
                nx, ny = x + dx, y + dy
                temp_sum += graph[nx][ny]
            result = max(result, temp_sum)
        except IndexError:
            continue

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 1, graph[i][j])  # 시작점 포함
        visited[i][j] = False
        exce(i, j)

print(result)