# 소프티어 - 장애물 인식 프로그램 (Lv2)
# dfs 풀이 - 아직 미완!!
import sys
std = sys.stdin;

k = int(std.readline());

map_array = [];
for i in range(0,k):
  map_array.append(list(map(int ,std.readline().strip())))

answer_arr =[];

dx = [-1,0,1,0];
dy = [0,-1,0,1];

cnt = 1;
def dfs(x,y):
  #상하좌우 이동
  for i in range(0,4):
    _x = x + dx[i];
    _y = y + dy[i];
    if ( _x >= 0 and _y >= 0 and _x < k and _y < k ):
      if ( map_array[_x][_y] == 1 ): 
        #dfs 호출
        #방문 여부 판단위해 지나온 장애물은 0으로 
        global cnt;
        cnt= cnt+1;
        map_array[_x][_y] =0;
        dfs(_x, _y);

for i in range(0,k):
  for j in range(0,k):
    if (map_array[i][j] == 1):
      map_array[i][j] =0;
      dfs(i,j);
      answer_arr.append(cnt);
      cnt=1;
      
print(len(answer_arr));
answer_arr.sort();
for i in answer_arr:
  print(i)