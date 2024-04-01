# 7562 - 나이트의 이동(실버1)
from sys import stdin as s
from collections import deque

#제출 시 주석 필수
s=open("input.txt","rt") 

n= int(s.readline());

dx=[1,1,2,2,-1,-1,-2,-2];
dy=[2,-2,1,-1,2,-2,1,-1];

for _ in range(n):
    k=int(s.readline());
    [start_x, start_y] = list(map(int, s.readline().split(' ')))
    [end_x, end_y] = list(map(int, s.readline().split(' ')))
    visited=[[0 for _ in range(k)] for _ in range(k)]
    #최단거리 => bfs
    q=deque();
    q.append([start_x, start_y, 0])
    visited[start_x][start_y] = 1;
    while(q):
        [cur_x, cur_y, cnt] = q.popleft();   
        if (cur_x == end_x and cur_y == end_y):
            print(cnt);
            break;
        for i in range(8):
            _x = cur_x+dx[i];
            _y = cur_y+dy[i];
            if (_x >=0 and _y >=0 and _x < k and _y < k):
                if (visited[_x][_y] == 0):
                        visited[_x][_y] = 1;
                        q.append([_x, _y, cnt+1])
            
    
        