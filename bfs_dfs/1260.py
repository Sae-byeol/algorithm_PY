# 1260 - dfs와 bfs (실버2)
from sys import stdin as s
from collections import deque;
#제출 시 주석 필수
s=open("input.txt","rt")

[n,m,v] = list(map(int, s.readline().split(' ')));

#양방향 그래프
graph= [[] for _ in range(n+1)];

for i in range(m):
    [a,b] = list(map(int, s.readline().split(' ')));
    graph[a].append(b);
    graph[b].append(a);
    
for g in graph:
    g.sort();

visited_dfs=[0 for _ in range(n+1)];
dfs_answer=[];
def dfs(v):
    visited_dfs[v]=1;
    dfs_answer.append(v);
    #v와 연결된 점들
    for p in graph[v]:
        if (visited_dfs[p] == 0):
            #방문 안했다면 그 점으로 파고 들어가기
            dfs(p);
            
visited_bfs=[0 for _ in range(n+1)];
bfs_answer =[];
queue=deque();
def bfs():
    while queue:
        cur = queue.popleft();
        bfs_answer.append(cur);
        for p in graph[cur]:
            if (visited_bfs[p] == 0):
                visited_bfs[p] =1;
                queue.append(p);    
    
#start 
dfs(v);
print(*dfs_answer)
#start
queue.append(v);
visited_bfs[v]=1;
bfs();
print(*bfs_answer)
    
    