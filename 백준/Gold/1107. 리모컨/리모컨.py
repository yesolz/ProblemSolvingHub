import sys
input = sys.stdin.readline

def is_valid(channel, broken):
    for char in str(channel):
        if int(char) in broken:
            return False
    return True

def min_button(target, broken):
    min_presses = abs(target - 100)
    for channel in range(1000000):
        if is_valid(channel, broken):
            min_presses = min(min_presses, len(str(channel)) + abs(channel - target))
    return min_presses


N = int(input().rstrip())
M = int(input().rstrip())
if M > 0:
    broken = list(map(int, input().split()))
else:
    broken = []

print(min_button(N, broken))