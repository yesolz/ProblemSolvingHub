N, r, c = map(int, input().split())

def recursive(n, row, col):
    if n == 0:
        return 0
    count = 2 * (row % 2) + (col % 2)
    return 4 * recursive(n-1, row // 2, col // 2) + count

print(recursive(N, r, c))