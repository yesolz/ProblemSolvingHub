import sys
input = sys.stdin.readline

N = int(input().strip())
paper = [list(map(int, input().split())) for _ in range(N)]
white = 0
blue = 0

def cut(row, col, n):
    global white, blue
    color = paper[row][col]
    for i in range(row, row + n):
        for j in range(col, col + n):
            if color != paper[i][j]:
                cut(row, col, n // 2)         # 1사분면
                cut(row, col + n // 2, n // 2) # 2사분면
                cut(row + n // 2, col, n // 2) # 3사분면
                cut(row + n // 2, col + n // 2, n // 2) # 4사분면
                return
    if color == 0:
        white += 1
    else:
        blue += 1

cut(0, 0, N)
print(f"{white}\n{blue}")