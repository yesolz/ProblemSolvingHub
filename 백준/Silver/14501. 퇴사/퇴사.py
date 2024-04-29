n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

profit = 0

def dfs(index, current_profit):
    global profit, n, graph
    if index == n:
        profit = max(profit, current_profit)
        return
    # 현재 상담을 선택하는 경우 (상담이 끝나는 날짜로 점프)
    if index + graph[index][0] <= n:
        dfs(index + graph[index][0], current_profit + graph[index][1])
    # 현재 상담을 선택하지 않는 경우 (다음 날로 이동)
    dfs(index + 1, current_profit)

# 첫 번째 날부터 시작
dfs(0, 0)

print(profit)
