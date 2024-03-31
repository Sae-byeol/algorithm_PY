#11724 - 연결요소의 개수(실버2)
from sys import stdin as s
import sys
#제출 시 주석 필수
s=open("input.txt","rt");
sys.setrecursionlimit(10 ** 6); #재귀 런타임 에러 해결

def dfs(n):
    cur_arr=graph[n];
    for c in cur_arr:
        if(visited[c] == 0):
            visited[c] =1;
            dfs(c);
    
    return;

[point_cnt, line_cnt] = list(map(int, s.readline().split(' ')));

graph=[[] for _ in range(point_cnt+1)]
visited=[0 for _ in range(point_cnt+1)]
answer=0;
#무방향 그래프 생성
for _ in range(line_cnt):
    [a,b] = list(map(int, s.readline().split(' ')))
    graph[a].append(b);
    graph[b].append(a);

#시작
for i in range(1, point_cnt+1):
    if(visited[i]==0):
        answer+=1;
        dfs(i);
print(answer)
    

    