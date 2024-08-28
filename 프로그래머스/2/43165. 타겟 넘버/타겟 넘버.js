function solution(numbers, target) {

    function dfs(index, cur_sum) {
        if (index === numbers.length) {
            if (cur_sum === target) {
                return 1
            } else {
                return 0
            }
        }
        
        const add = dfs(index + 1, cur_sum + numbers[index])
        const subtract = dfs(index + 1, cur_sum - numbers[index])
        
        return add + subtract
    }
    
    return dfs(0, 0)
    
}