import sys, copy
input = sys.stdin.readline
deepcopy = copy.deepcopy
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]


def up(board):
    for j in range(N):
        cursor = 0
        for i in range(1, N):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                # 커서가 가리키는 수가 0
                if board[cursor][j] == 0:
                    board[cursor][j] = tmp
                # 커서가 가리키는 수와 현재 위치의 수가 같을 때
                elif board[cursor][j] == tmp:
                    board[cursor][j] *= 2
                    cursor += 1
                # 다를 때
                else:
                    cursor += 1
                    board[cursor][j] = tmp
    return board

def down(board):
    for j in range(N):
        cursor = N-1
        for i in range(N-2, -1, -1):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                # 커서가 가리키는 수가 0
                if board[cursor][j] == 0:
                    board[cursor][j] = tmp
                # 커서가 가리키는 수와 현재 위치의 수가 같을 때
                elif board[cursor][j] == tmp:
                    board[cursor][j] *= 2
                    cursor -= 1
                # 다를 때
                else:
                    cursor -= 1
                    board[cursor][j] = tmp
    return board

def left(board):
    for i in range(N):
        cursor = 0
        for j in range(1, N):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                # 커서가 가리키는 수가 0
                if board[i][cursor] == 0:
                    board[i][cursor] = tmp
                # 커서가 가리키는 수와 현재 위치의 수가 같을 때
                elif board[i][cursor] == tmp:
                    board[i][cursor] *= 2
                    cursor += 1
                # 다를 때
                else:
                    cursor += 1
                    board[i][cursor] = tmp
    return board

def right(board):
    for i in range(N):
        cursor = N-1
        for j in range(N-2, -1, -1):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                # 커서가 가리키는 수가 0
                if board[i][cursor] == 0:
                    board[i][cursor] = tmp
                # 커서가 가리키는 수와 현재 위치의 수가 같을 때
                elif board[i][cursor] == tmp:
                    board[i][cursor] *= 2
                    cursor -= 1
                # 다를 때
                else:
                    cursor -= 1
                    board[i][cursor] = tmp
    return board

def dfs(board, chance):
    if chance == 5:
        return max(map(max, board))
    return max(dfs(up(deepcopy(board)), chance + 1), dfs(down(deepcopy(board)), chance + 1), dfs(left(deepcopy(board)), chance + 1), dfs(right(deepcopy(board)), chance + 1))

print(dfs(board, 0))