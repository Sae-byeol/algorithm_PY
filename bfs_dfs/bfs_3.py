# 소프티어 - 장애물 인식 프로그램 (Lv2)
# bfs 풀이
import sys
from collections import deque
std = sys.stdin;

k = int(std.readline());

map_array = [];
for i in range(0,k):
  map_array.append(list(map(int ,std.readline().strip())))

answer_arr =[];

dx = [-1,0,1,0];
dy = [0,-1,0,1];

def bfs(x,y):
  q = deque();
  q.append([x,y])
  cnt = 1; 
  while q:
    [cur_x, cur_y] = q.popleft();
    for i in range(0,4):
      _x = cur_x + dx[i];
      _y = cur_y + dy[i];
      if (_x >=0 and _y >=0 and _x < k and _y < k):
        if (map_array[_x][_y] == 1):
          cnt=cnt+1;
          map_array[_x][_y] = 0;
          q.append([_x, _y])
  answer_arr.append(cnt);
      
for i in range(k):
  for j in range(k):
    if (map_array[i][j] == 1):
    #자기 자신도 방문처리 잊지말기
      map_array[i][j] = 0;
      bfs(i,j);

answer_arr.sort();
print(len(answer_arr));
for a in answer_arr:
  print(a)
    
  