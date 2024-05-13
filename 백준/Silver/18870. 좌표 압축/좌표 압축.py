n = int(input())
lst = list(map(int, input().split()))
sorted_lst = sorted(lst)

dct = dict()

count = 0
for i in range(len(sorted_lst)):
    if sorted_lst[i] not in dct:
        dct[sorted_lst[i]] = count
        count += 1

for i in range(len(lst)):
    print(dct[lst[i]], end=' ')