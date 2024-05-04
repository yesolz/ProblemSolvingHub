# 피보나치 함수

t = int(input())

def count_ways(n):
    count_zero = [1, 0]
    count_one = [0, 1]

    for i in range(2, n+1):
        count_zero.append(count_zero[i-1] + count_zero[i-2])
        count_one.append(count_one[i-1] + count_one[i-2])

    return count_zero[n], count_one[n]


# 입출력
results = []
for _ in range(t):
    n = int(input())
    results.append(count_ways(n))

for r in results:
    print(r[0], r[1])