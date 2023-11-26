# 1753 - 최단 경로
from sys import stdin as s
import heapq
#제출 시 주석 필수
s=open("input.txt","rt") #절대 경로도 되고, 상대 경로도 된다. # r read t text 
                        
[point_num, input_num] = list(map(int, s.readline().split(' ')));
start = int(s.readline());
graph=[[] for _ in range(point_num+1)]
for _ in range(input_num):
    e,v,w=map(int,s.readline().split())
    graph[e].append([w,v]) 
    
def dijkstra(start):
    INF=1e9;
    #방문체크 배열 (INF로 초기화)
    visited=[INF] * (point_num+1); 
    visited[start] = 0;
     
    queue=[[0, start]];
    while(queue):
        cost, node= heapq.heappop(queue);
        if cost > visited[node]: 
            #볼 필요 없음 
            continue;
        # 해당 점에 연결된 간선들 하나씩 살펴보기
        for k,u in graph[node]:
            if visited[u] > visited[node]+k: # 이동 비용이 작다면
                visited[u] = visited[node]+k # 그렇게 이동
                heapq.heappush(queue,[visited[u], u])
    return visited[1:]

for ans in dijkstra(start): 
  print(ans if ans!=1e9 else 'INF')