from collections import deque

gears = [deque(map(int, input().strip())) for _ in range(4)]
k = int(input())
commands = [tuple(map(int, input().split())) for _ in range(k)]

def rotate(gear, direction):
    if direction == 1:  # 시계 방향
        gear.appendleft(gear.pop())
    elif direction == -1:  # 반시계 방향
        gear.append(gear.popleft())

for gear_num, direction in commands:
    gear_num -= 1
    rotations = [0] * 4
    rotations[gear_num] = direction

    for i in range(gear_num, 0, -1):
        if gears[i][6] != gears[i - 1][2]:  # 극이 다르면
            rotations[i - 1] = -rotations[i]
        else:
            break

    for i in range(gear_num, 3):
        if gears[i][2] != gears[i + 1][6]:  # 극이 다르면
            rotations[i + 1] = -rotations[i]
        else:
            break

    # 회전 
    for i in range(4):
        if rotations[i] != 0:
            rotate(gears[i], rotations[i])

score = 0
for i in range(4):
    if gears[i][0] == 1:
        score += 2**i

print(score)