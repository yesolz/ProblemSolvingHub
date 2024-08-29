function solution(n, computers) {
    
    function dfs(node){
        visited[node] = true
        for (let i=0; i<n; i++){
            if (!visited[i] && computers[node][i] === 1) {
                dfs(i)
            }
        }
    }
    
    
    visited = Array(n).fill(false)
    
    let answer = 0;
    
    for (let i=0; i<n; i++){
        if (!visited[i]) {
            dfs(i)
            answer += 1
        }
    }
    
    
    
    return answer;
}