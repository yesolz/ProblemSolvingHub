dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2

for i in range(6, 101):
    dp[i] = dp[i-1] + dp[i-5]

t = int(input()) # 테스트 케이스 개수
for _ in range(t):
    n = int(input())
    print(dp[n])
