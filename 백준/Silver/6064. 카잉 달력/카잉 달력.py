import sys
import math

input = sys.stdin.readline
T = int(input())

def cal(M, N, x, y):
    lcm = abs(M*N) // math.gcd(M, N)
    while x <= lcm:
        if (x - 1) % N + 1 == y:
            print(x)
            return
        x += M
    print(-1)



for _ in range(T):
    M, N, x, y = list(map(int, input().split()))
    cal(M, N, x, y)