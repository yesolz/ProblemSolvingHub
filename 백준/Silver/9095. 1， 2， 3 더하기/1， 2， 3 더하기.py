def count_ways(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return count_ways(n-1) + count_ways(n-2) + count_ways(n-3)

T = int(input())
results = []

for _ in range(T):
    n = int(input())
    results.append(count_ways(n))

for result in results:
    print(result)