def count_dis(mbti1, mbti2):
    """ 두 MBTI 유형 사이의 거리를 계산하는 함수 """
    return sum(1 for a, b in zip(mbti1, mbti2) if a != b)

def find_minimum_distance(N, students):
    if N > 32:
        return 0

    min_distance = float('inf')
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                dis_ij = count_dis(students[i], students[j])
                dis_jk = count_dis(students[j], students[k])
                dis_ik = count_dis(students[i], students[k])
                total_distance = dis_ij + dis_jk + dis_ik
                if total_distance < min_distance:
                    min_distance = total_distance
    return min_distance

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    students = input().strip().split()
    print(find_minimum_distance(N, students))
