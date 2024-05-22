from collections import deque
import sys

input = sys.stdin.readline

def bfs(a, b):
    queue = deque([(a, "")])
    visited = [False] * 10000
    visited[a] = True

    while queue:
        cur, commands = queue.popleft()

        if cur == b:
            return commands

        # 명령어 D
        next_a = (2 * cur) % 10000
        if not visited[next_a]:
            visited[next_a] = True
            queue.append((next_a, commands + "D"))

        # 명령어 S
        next_a = cur - 1 if cur != 0 else 9999
        if not visited[next_a]:
            visited[next_a] = True
            queue.append((next_a, commands + "S"))

        # 명령어 L
        next_a = (cur % 1000) * 10 + cur // 1000
        if not visited[next_a]:
            visited[next_a] = True
            queue.append((next_a, commands + "L"))

        # 명령어 R
        next_a = (cur // 10) + (cur % 10) * 1000
        if not visited[next_a]:
            visited[next_a] = True
            queue.append((next_a, commands + "R"))

t = int(input().strip())
results = []

for _ in range(t):
    a, b = map(int, input().split())
    results.append(bfs(a, b))

print('\n'.join(results))