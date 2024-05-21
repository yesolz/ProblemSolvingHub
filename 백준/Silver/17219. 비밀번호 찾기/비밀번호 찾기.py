import sys
input = sys.stdin.readline

N, M = map(int, input().split())
memo = dict()
for _ in range(N):
    key, value = input().split()
    memo[key] = value

for _ in range(M):
    find = input().rstrip()
    print(memo[find])