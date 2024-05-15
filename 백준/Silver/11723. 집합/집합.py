import sys
input = sys.stdin.readline
M = int(input().strip())
s = set()

for _ in range(M):
    command = input().strip().split()
    if len(command) == 2:
        op, x = command[0], int(command[1])
        if op == "add":
            s.add(x)
        elif op == "remove":
            s.discard(x)
        elif op == "check":
            print(1 if x in s else 0)
        elif op == "toggle":
            if x in s:
                s.remove(x)
            else:
                s.add(x)
    else:
        if command[0] == "all":
            s.update(range(1, 21))
        elif command[0] == "empty":
            s.clear()