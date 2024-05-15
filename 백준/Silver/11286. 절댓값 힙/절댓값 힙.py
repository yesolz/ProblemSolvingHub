import sys
import heapq

input = sys.stdin.readline
heap = []

N = int(input().strip())
for _ in range(N):
    x = int(input().strip())
    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)