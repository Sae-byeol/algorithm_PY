# 프로그래머스 - 최단거리
from collections import deque
def solution(maps):
    answer = 0
    
    mapx=len(maps)
    mapy=len(maps[0])
    visited = [[0] * mapy for i in range(mapx)]
    
    #상하좌우
    dx=[0,-1,0,1]
    dy=[1,0,-1,0]
    
    #초기 세팅
    q=deque();
    q.append([0,0]);
    visited[0][0]= 1;
    
    #start
    while q:
        y,x = q.popleft();
        #상하좌우 이동
        for i in range(0,4):
            nx = x+dx[i];
            ny= y+dy[i];
            #인덱스 유효성 검사
            if ( 0 <= ny < mapx and 0<=nx<mapy):
                #방문 여부 및 벽인지 검사
                if (visited[ny][nx] == 0 and maps[ny][nx] == 1):
                    #이동 가능 - 방문처리 하고 큐에 삽입
                    visited[ny][nx] = visited[y][x]+1
                    q.append([ny, nx]);
    if (visited[mapx-1][mapy-1] == 0):
        #실패한 경우
        answer = -1;
    else:
        answer= visited[mapx-1][mapy-1];
    
    return answer;