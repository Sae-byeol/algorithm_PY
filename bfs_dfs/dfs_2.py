# 프로그래머스 - 네트워크 (dfs)
def solution(n, computers):
    answer = 0
    #dfs 풀이
    visited=[]
    def dfs(num):
        visited.append(num);
        for i in range(0, n):
            if (i not in visited and computers[num][i] == 1):
                dfs(i);
            
    for i in range(0, n):
        if(i not in visited):
            dfs(i);
            answer+=1;
        
    return answer