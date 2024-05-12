import sys
input = sys.stdin.readline

n, m = map(int, input().split())

p_dict = {}

# 포켓몬 번호 1부터 시작
for i in range(1, n+1):
    name = input().rstrip()
    p_dict[i] = name
    p_dict[name] = i

for _ in range(m):
    x = input().rstrip()

    if x.isdigit():
        x = int(x)
        if x in p_dict:
            print(p_dict[x])
    else:
        print(p_dict[x])