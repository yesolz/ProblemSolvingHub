from collections import deque

import sys
input = sys.stdin.readline

def snakes_and_ladders(N, M, ladders, snakes):
    board = list(range(101))

    for start, end in ladders.items():
        board[start] = end

    for start, end in snakes.items():
        board[start] = end

    queue = deque([(1, 0)]) # (현재 위치, 주사위 횟수)
    visited = [False] * 101
    visited[1] = True

    while queue:
        position, dice = queue.popleft()

        if position == 100:
            return dice

        for i in range(1, 7):
            next_pos = position + i
            if next_pos <= 100:
                next_pos = board[next_pos]
                if not visited[next_pos]:
                    visited[next_pos] = True
                    queue.append((next_pos, dice + 1))


N, M = map(int, input().split())
ladders = {}
for _ in range(N):
    x, y = map(int, input().split())
    ladders[x] = y
snakes = {}
for _ in range(M):
    u, v = map(int, input().split())
    snakes[u] = v

print(snakes_and_ladders(N, M, ladders, snakes))