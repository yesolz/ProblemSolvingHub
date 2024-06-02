def solve_n_queens(n):
    def backtrack(row, cols, diag1, diag2):
        if row == n:
            return 1
        count = 0
        available_positions = ((1 << n) - 1) & ~(cols | diag1 | diag2)
        while available_positions:
            position = available_positions & -available_positions
            available_positions -= position
            count += backtrack(row + 1, cols | position, (diag1 | position) << 1, (diag2 | position) >> 1)
        return count

    return backtrack(0, 0, 0, 0)

N = int(input())
print(solve_n_queens(N))
