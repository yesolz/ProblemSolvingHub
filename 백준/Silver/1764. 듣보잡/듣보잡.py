import sys
input = sys.stdin.readline

n, m = map(int, input().split())

n_list = {input() for _ in range(n)}
m_list = {input() for _ in range(m)}
total = n_list & m_list
result = sorted(list(total))
print(len(result))
for i in result:
    print(i, end ='')