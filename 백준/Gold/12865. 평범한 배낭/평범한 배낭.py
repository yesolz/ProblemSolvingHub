import sys
input = sys.stdin.readline

def knapsack(n, k, items):
    dp = [[0] * (k+1) for _ in range(n+1)]
    for i in range(1, n+1):
        weight, value = items[i-1]
        for w in range(k+1):
            if w >= weight:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight] + value)
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][k]

n, k = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(n)]

print(knapsack(n, k, items))
