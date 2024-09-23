n = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_value = -int(1e9)
min_value = int(1e9)

def dfs(i, num):
    global add, sub, mul, div, max_value, min_value

    if i == n:
        max_value = max(max_value, num)
        min_value = min(min_value, num)

    else:
        if add > 0:
            add -= 1
            dfs(i + 1, num + numbers[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, num - numbers[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1,  num * numbers[i])
            mul += 1
        if div > 0:
            div -= 1
            if num < 0:
                num = -(-num // numbers[i])
            else:
                num //= numbers[i]
            dfs(i + 1, num)
            div += 1

dfs(1, numbers[0])

print(max_value)
print(min_value)