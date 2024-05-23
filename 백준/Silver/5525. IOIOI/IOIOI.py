N = int(input())
M = int(input())
S = input()

def count_pn(N, S):
    pattern_count = 0
    i = 0
    count = 0

    while i < len(S) - 1:
        if S[i:i+3] == "IOI":
            count += 1
            i += 2 # 다음 I로 이동
            if count == N:
                pattern_count += 1
                count -= 1 # 패턴 중첩될 수도 있으므로
        else:
            count = 0
            i += 1

    return pattern_count

print(count_pn(N, S))