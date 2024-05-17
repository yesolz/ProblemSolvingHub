import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for i in range(T):
    instruction = input().rstrip()
    n = int(input())
    lst = deque(input().rstrip()[1:-1].split(","))

    if n == 0:
        lst = deque()  # 빈 경우 명시적으로 deque를 초기화

    reverse_flag = False  # 현재 뒤집힌 상태인지를 나타내는 플래그
    error_flag = False  # 에러 발생 여부를 나타내는 플래그

    for j in instruction:
        if j == 'R':
            reverse_flag = not reverse_flag  # 뒤집기 상태 토글
        elif j == 'D':
            if lst:
                if reverse_flag:
                    lst.pop()  # 뒤집힌 상태이면 오른쪽 요소 제거
                else:
                    lst.popleft()  # 정상 상태이면 왼쪽 요소 제거
            else:
                print("error")  # 에러 출력
                error_flag = True
                break

    if not error_flag:
        # 모든 명령 처리 후 최종 출력
        if reverse_flag:
            lst.reverse()  # 최종적으로 뒤집어야 할 경우에만 뒤집기
        print("["+",".join(lst)+"]")
