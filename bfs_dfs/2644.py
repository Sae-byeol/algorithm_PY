# 2644 - 촌수(실버2)
from sys import stdin as s

#제출 시 주석 필수
s=open("input.txt","rt") 

total = int(s.readline());
[n,m] = list(map(int, s.readline().split(' ')));
k= int(s.readline());

#양방향 그래프 생성
graph=[[] for _ in range(total+1)];
for i in range(k):
    [a,b] = list(map(int, s.readline().split(' ')));
    graph[a].append(b);
    graph[b].append(a);

answer= [];
visited = [0 for _ in range(total+1)]

#dfs - 그래프 탐색 , 이때의 탐색 cnt 가 촌수
def dfs(num, cnt):
    #찾음
    if (num == m):
        answer.append(cnt)
        return;
    visited[num] = 1;
    cnt+=1;
    for i in graph[num]:
        if (visited[i] == 0):
            #방문 안한 점이라면 탐색
            dfs(i, cnt);

#start
dfs(n, 0);
if (len(answer) == 0):
    print(-1);
else:
    print(answer[0])