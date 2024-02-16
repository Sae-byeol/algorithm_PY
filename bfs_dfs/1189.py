# 1189 - 컴백홈 (실버1)
from sys import stdin as s
#제출 시 주석 필수
s=open("input.txt","rt")

[r,c,k] = list(map(int, s.readline().split(' ')));
input_arr = [[0 for _ in range(c)] for _ in range(r)];

for i in range(r):
    str=s.readline();
    for j in range(c):
        input_arr[i][j] = str[j]

dx=[0,1,0,-1];
dy=[1,0,-1,0];
answer = 0;
def dfs(x,y, cnt):
    global answer;
    if (x == 0 and y == c-1):
        if (cnt == k):
            answer+=1;
        return;
    
    #동서남북 이동
    for i in range(4):
        _x=x+dx[i];
        _y=y+dy[i];
        if (_x >= 0 and _y>=0 and _x<r and _y < c):
            #방문 가능 체크
            if (input_arr[_x][_y] != 'T'):
                input_arr[_x][_y] = 'T' #방문 기록
                dfs(_x, _y, cnt+1);
                input_arr[_x][_y] = '.' #다른 경로 탐색에 영향 주지 않도록 되돌리기
    
#start
#시작점 방문 체크 해주고 시작하기
input_arr[r-1][0] = 'T' 
dfs(r-1, 0, 1);
print(answer)