# 프로그래머스 - 네트워크(bfs)
from collections import deque
def solution(n, computers):
    answer = 0
    #bfs 풀이
    visited=[];
    def bfs(num):
        queue=deque();
        queue.append(num);
        while len(queue) > 0:
            cur = queue.popleft();
            visited.append(cur);
            for i in range(0,n):
                if (i not in visited and computers[cur][i]):
                    print(i)
                    queue.append(i)#while문 끝나지 않도록 큐에 삽입 
    for i in range(0,n):
        if(i not in visited):
            bfs(i);
            answer+=1;

    return answer