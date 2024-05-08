from collections import deque

def bfs(n, k):
    if n == k:
        return 0

    visited = [False] * 100001
    queue = deque([(n, 0)])

    while queue:
        cur, time = queue.popleft()

        # X - 1
        if cur > 0 and not visited[cur - 1]:
            if cur - 1 == k:
                return time + 1
            visited[cur - 1] = True
            queue.append((cur - 1, time + 1))

        # X + 1
        if cur < 100000 and not visited[cur + 1]:
            if cur + 1 == k:
                return time + 1
            visited[cur + 1] = True
            queue.append((cur + 1, time + 1))

        # 2 * X
        if cur * 2 <= 100000 and not visited[cur * 2]:
            if cur * 2 == k:
                return time + 1
            visited[cur * 2] = True
            queue.append((cur * 2, time + 1))

n, k = map(int, input().split())

print(bfs(n, k))