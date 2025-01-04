# 14499 주사위 굴리기 

def roll_dice(dice, direction):
    top, north, east, west, south, bottom = dice

    if direction == 1: # 동
        dice[0] = west
        dice[2] = top
        dice[3] = bottom
        dice[5] = east
    elif direction == 2: # 서
        dice[0] = east
        dice[2] = bottom
        dice[3] = top
        dice[5] = west
    elif direction == 3: # 북
        dice[0] = south
        dice[1] = top
        dice[4] = bottom
        dice[5] = north
    else: # 남
        dice[0] = north
        dice[1] = bottom
        dice[4] = top
        dice[5] = south

N, M, X, Y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

# 주사위 초기 상태
dice = [0, 0, 0, 0, 0, 0]

# 동, 서, 북, 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

cur_x, cur_y = X, Y

for command in commands:
    direction = command - 1

    next_x = cur_x + dx[direction]
    next_y = cur_y + dy[direction]

    if next_x < 0 or next_x >= N or next_y < 0 or next_y >= M:
        continue

    # 주사위 굴리기!
    roll_dice(dice, command)

    # 값 바꾸기
    if board[next_x][next_y] == 0:
        board[next_x][next_y] = dice[5]
    else:
        dice[5] = board[next_x][next_y]
        board[next_x][next_y] = 0

    # 현재 위치
    cur_x, cur_y = next_x, next_y

    # 출력
    print(dice[0])