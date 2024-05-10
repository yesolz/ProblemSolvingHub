import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

low, high = 0, max(trees)

while low <= high:
    mid = (low + high) // 2
    total = sum((tree - mid) for tree in trees if tree > mid)

    if total >= M:
        low = mid + 1
    else:
        high = mid - 1

print(high)