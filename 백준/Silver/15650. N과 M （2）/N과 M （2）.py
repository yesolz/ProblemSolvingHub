import itertools

n, m = map(int, input().split())
numbers = list(range(1, n+1))
combinations = list(itertools.combinations(numbers, m))
for c in combinations:
    print(" ".join(map(str, c)))