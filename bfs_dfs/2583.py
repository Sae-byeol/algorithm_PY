# 2583 - 영역구하기(실버1) 
from sys import stdin as s
import sys
#제출 시 주석 필수
s=open("input.txt","rt");
sys.setrecursionlimit(10 ** 6); #재귀 런타임 에러 해결

dx=[-1,0,1,0];
dy=[0,1,0,-1];

def dfs(i,j, num):
    graph[i][j] = num;
    for _i in range(4):
        _x = i+dx[_i];
        _y = j+dy[_i];
        if (_x < n and _y < m and _x >=0 and _y >= 0):
            if (graph[_x][_y] == 0):
                dfs(_x, _y, num);
    return;

[m,n,k] = list(map(int, s.readline().split(' ')))

graph = [[0 for _ in range(m)] for _ in range(n)];

for _ in range(k):
    [a,b,c,d] = list(map(int, s.readline().split(' ')))
    for i in range(a, c):
        for j in range(b, d):
            graph[i][j] = -1;

index=0;
for i in range(n):
    for j in range(m):
        if (graph[i][j] ==0):
            index+=1;
            dfs(i,j, index)
            
total_cnt =index; 
answer_arr=[];
for num in range(1, total_cnt+1):
    cnt=0;
    for i in range(n):
        for j in range(m):
            if (graph[i][j] == num):
                cnt+=1;
    answer_arr.append(cnt);

print(total_cnt);
print(*sorted(answer_arr))

    