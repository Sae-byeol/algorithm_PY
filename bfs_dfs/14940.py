# 14940 - 쉬운 최단거리 (실버1)
from sys import stdin as s
from collections import deque;
#제출 시 주석 필수
s=open("input.txt","rt")

[n,m] = list(map(int, s.readline().split(' ')))
graph=[[0 for _ in range(m)] for _ in range(n)];

queue= deque();

dx=[0,1,0,-1];
dy=[1,0,-1,0];

for i in range(n):
    graph[i] = list(map(int, s.readline().split(' ')));

start_index =[]

visited=[[0 for _ in range(m)] for _ in range(n)];
answer=[[-1 for _ in range(m)] for _ in range(n)];
for i in range(n):
    for j in range(m):
        if (graph[i][j] == 2):
            start_index= [i, j];
            break;

def bfs():
    while queue:
        [cur_index, cur_cnt] = queue.popleft();
        answer[cur_index[0]][cur_index[1]]=cur_cnt;
        #연결된 점 찾기
        for i in range(0,4):
            _x= cur_index[0]+dx[i];
            _y= cur_index[1]+dy[i];
            if (_x >= 0 and _y >=0 and _x<n and _y < m ):
                if ( graph[_x][_y] == 1):
                    if (visited[_x][_y] == 0):
                        visited[_x][_y] =1;
                        queue.append([[_x, _y], cur_cnt+1])

for i in range(n):
    for j in range(m):
        if (graph[i][j] == 0):
            answer[i][j] =0;     
#start
queue.append([start_index, 0])
visited[start_index[0]][start_index[1]] =1;
bfs()
for a in answer :
    print(*a)
    

