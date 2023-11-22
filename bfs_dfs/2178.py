# 2178 - 미로탐색 (실버1)
from sys import stdin as s
from collections import deque

#제출 시 주석 필수
s=open("input.txt","rt") #절대 경로도 되고, 상대 경로도 된다. # r read t text 
                        
[n, m]=list(map(int, s.readline().split(' ')));

# 한 줄 입력받고, 우측 \n을 제거한 후, 모든 원소를 int형으로 변환한 배열을 생성한다.
graph = [list(map(int, s.readline().rstrip())) for _ in range(n)]

#간선의 가중치가 모두 1 + 최단 거리 or 최소 비용 => "BFS"
queue = deque();

#상하좌우
dx=[-1,0,1,0]
dy=[0,-1,0,1]       

#시작
queue.append([0,0]);

while(queue):
    [x, y] = queue.popleft();
    if (x == n-1 and y == m-1):
        print(graph[x][y]);
        break;
    #상하좌우 이동
    for i in range(0,4):
        _x= x+dx[i];
        _y = y+dy[i];
        #범위 체크
        if (_x >=0 and _y >=0 and _x < n and _y < m and graph[_x][_y] != 0):
            #  방문 안했던 점으로 한 칸 앞으로 이동
            if (graph[_x][_y] == 1):
                queue.append([_x, _y]);
                graph[_x][_y] = graph[x][y]+1;

        
