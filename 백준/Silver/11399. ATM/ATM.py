n = int(input())
time = list(map(int, input().split()))
time = sorted(time)

lst = []
cost = 0
for i in range(len(time)):
    cost += time[i]
    lst.append(cost)

print(sum(lst))