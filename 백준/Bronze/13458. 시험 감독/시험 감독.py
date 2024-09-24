n = int(input())
people = list(map(int, input().split()))
b, c = map(int, input().split())

res = 0

for i in range(n):
    people[i] -= b
    res += 1
    if people[i] > 0:
        if people[i] % c == 0:
            res += (people[i] // c)
        else:
            res += (people[i] // c + 1)
            
print(res)