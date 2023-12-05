# 10026 - 적록색약 (골드5)
from sys import stdin as s
from collections import deque
import copy
#제출 시 주석 필수
s=open("input.txt","rt");

k = int(s.readline());
input_arr =[];
for i in range(0,k):
    input_arr.append(list(map(str,str(s.readline().strip()) )));

#색약을 위한 배열 (이차원배열의 얕은 복사 - deepcopy())
blind_arr = copy.deepcopy(input_arr)
for i in range(0, k):
    for j in range(0,k):
        #g를 r로
        if (blind_arr[i][j] == 'G'):
            blind_arr[i][j]= 'R'
        
dx=[-1,0,1,0];
dy=[0,-1,0,1];

q=deque();

def bfs(color, arr):
    while q: 
        [x,y]= q.popleft();
        #상하좌우 이동
        for i in range(0,4):
            _x=x+dx[i];
            _y=y+dy[i];
            if (_x >=0 and _y >=0 and _x <k and _y < k):
                if (arr[_x][_y] == color):
                    #같은 색이면 전개
                    arr[_x][_y] = -1;
                    q.append([_x, _y]);

count =0;
blind_count =0;
for i in range(0, k):
    for j in range(0,k):
        if (input_arr[i][j] != -1):
            q.append([i,j]);
            color =  input_arr[i][j];
            input_arr[i][j] = -1;
            bfs(color, input_arr);
            count+=1;
q.clear();
for i in range(0, k):
    for j in range(0,k):
        if (blind_arr[i][j] != -1):
            q.append([i,j]);
            color =  blind_arr[i][j];
            blind_arr[i][j] = -1;
            bfs(color, blind_arr);
            blind_count+=1;

print(str(count) + ' ' + str(blind_count))
            