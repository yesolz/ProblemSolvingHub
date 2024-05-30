n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

def max_path(n, triangle):
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = triangle[0][0]

    for i in range(1, n):
        for j in range(i + 1):
            if j == 0: # 첫 번째 열
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == i: # 마지막 열
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

    return max(dp[n-1])

print(max_path(n, triangle))