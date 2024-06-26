import heapq
import sys
input = sys.stdin.readline

max_heap = []

for _ in range(int(input())):
    n = int(input())

    if n == 0:
        if len(max_heap):
            print(-heapq.heappop(max_heap))
        else:
            print(0)
    else:
        heapq.heappush(max_heap, -n)