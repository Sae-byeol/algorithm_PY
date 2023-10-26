# 2606 - 바이러스
from sys import stdin as s

#제출 시 주석 필수
s=open("input.txt","rt") #절대 경로도 되고, 상대 경로도 된다. # r read t text 
                        
node_number=int(s.readline());
line_number = int(s.readline());
array =[]
for i in range(0, line_number):
    array.append(list(map(int, s.readline().split(' '))))
    
graph=[[] for _ in range(node_number +1)];

for i in array:
    n1=i[0];
    n2=i[1];
    graph[n1]+=[n2];
    graph[n2]+=[n1];
    
visited =[];

def dfs(num):
    for i in graph[num]:
        if(i not in visited):
            visited.append(i)
            dfs(i);

#시작
for i in graph[1]:
    dfs(i);
    
if (len(visited) == 0): 
    answer =0;
else:
    answer=len(visited) -1 
print(answer)