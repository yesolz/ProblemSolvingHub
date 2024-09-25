N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

# 반시계 방향 회전
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

def clean(x, y, d):
    cnt = 0
    while True:

        # 1
        if room[x][y] == 0:
            room[x][y] = -1 # 청소함 표시
            cnt += 1

        # 2
        for _ in range(4):
            d = (d - 1) % 4
            nx, ny = x + dx[d], y + dy[d]
            if in_range(nx, ny) and room[nx][ny] == 0:
                x, y = nx, ny
                break # 1로

        else:
            x, y = x + dx[d] * (-1), y + dy[d] * (-1) # 후진
            if room[x][y] == 1 or not in_range(x, y):
                print(cnt) # 멈춤
                return

clean(r, c, d)