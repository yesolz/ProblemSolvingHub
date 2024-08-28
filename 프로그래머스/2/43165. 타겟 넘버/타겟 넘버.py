def solution(numbers, target):
    
    def dfs(index, cur_sum):
        
        # 모든 숫자 다 사용한 경우
        if index == len(numbers):
            # 끝까지 했을 때 타겟과 같다면 1 증가
            if cur_sum == target:
                return 1
            else:
                return 0
        
        # 현재 숫자에서 더하거나 / 빼는 방식 - 재귀적으로
        add = dfs(index+1, cur_sum + numbers[index])
        subtract = dfs(index+1, cur_sum - numbers[index])
        
        return add + subtract
    
    return dfs(0, 0)