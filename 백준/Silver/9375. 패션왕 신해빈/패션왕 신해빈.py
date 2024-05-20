import sys
input = sys.stdin.readline

result = []

testcases = int(input()) # 테스트케이스 개수

def combi(clothes_dict):
    count = 1 # 곱셈을 위한 초기값
    for clo_type in clothes_dict:
        count *= (len(clothes_dict[clo_type]) + 1)
    return count - 1 # 알몸인 경우 제외

for _ in range(testcases):
    n = int(input()) # 의상 수
    clothes = dict() # 각 테스트케이스마다 초기화
    for _ in range(n):
        name, clo_type = input().split()
        if clo_type in clothes:
            clothes[clo_type].append(name)
        else:
            clothes[clo_type] = [name] # 리스트로 초기화
    result.append(combi(clothes))

for c in result:
    print(c)