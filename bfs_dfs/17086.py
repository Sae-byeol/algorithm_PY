# 17086 - 아기상어2(실버2)
from sys import stdin as s
from collections import deque;
#제출 시 주석 필수
s=open("input.txt","rt")

[n,m] = list(map(int, s.readline().split(' ')));

input_arr = [[0 for _ in range(m)] for _ in range(n)];
ans=0;

dx=[-1,-1,-1,0,0,1,1,1]
dy=[-1,0,1,-1,1,-1,0,1]

for i in range(n):
    input_arr[i] = list(map(int, s.readline().split(' ')));

def bfs(x,y,count):
    queue=deque();
    visited=[[0 for _ in range(m)] for _ in range(n)];
    queue.append([[x,y], count]);
    visited[x][y] =1;
    while queue:
        [[cur_x, cur_y], cnt] = queue.popleft();
        for i in range(8):
            _x = cur_x+dx[i];
            _y = cur_y+dy[i];
            if (_x >= 0 and _y >= 0 and _x <n and _y <m):
                if (visited[_x][_y] == 0):
                    if (input_arr[_x][_y] ==1):
                        #찾음
                        return cnt+1;
                    else: 
                        queue.append([[_x, _y], cnt+1]);
                        visited[_x][_y] =1 ;
    
for i in range(n):
    for j in range(m):
        if (input_arr[i][j] == 0):
            ans = max(ans,bfs(i,j,0));
print(ans)
