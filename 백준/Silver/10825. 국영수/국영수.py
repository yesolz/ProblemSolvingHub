n = int(input())

# 정렬을 위해서 input 값의 타입 신경 써주어야 함

students = []

# 학생 정보 입력
for _ in range(n):
    name, kor, eng, math = input().split()
    students.append((name, int(kor), int(eng), int(math)))

# std_list = [input().split() for _ in range(n)]


sorted_list = sorted(students, key=lambda x: (-x[1], x[2], -x[3], x[0]))

# 결과 출력
for item in sorted_list:
    print(item[0])