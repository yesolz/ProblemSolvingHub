n, k = map(int, input().split())
lst = [int(input()) for _ in range(n)]
lst = sorted(lst, reverse=True)

total = 0
for i in range(n):
    x = k // lst[i]
    total += x
    k -= lst[i] * x

print(total)