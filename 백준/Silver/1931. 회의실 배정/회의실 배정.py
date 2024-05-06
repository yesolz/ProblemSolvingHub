n = int(input())
meeting = [list(map(int, input().split())) for _ in range(n)]
meeting.sort(key=lambda x: (x[1], x[0]))

selected = [meeting[0]]
end_time = meeting[0][1]

for m in meeting[1:]:
    if m[0] >= end_time:
        selected.append(m)
        end_time = m[1]

print(len(selected))
