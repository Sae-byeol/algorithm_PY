# 1149 - RGB 거리
from sys import stdin as s

#제출 시 주석 필수
s=open("input.txt","rt") #절대 경로도 되고, 상대 경로도 된다. # r read t text 
                        
number=int(s.readline());

cost_list = [list(map(int, s.readline().split(' '))) for _ in range(number)];

dp=[0]*(number+1);
r =[0]*(number+1);
g =[0]*(number+1);
b =[0]*(number+1);

for i in range(1, number+1):
    #i번째가 무슨색인지에 따라서 역추적
    r[i] = cost_list[i-1][0] + min(g[i-1], b[i-1]);
    g[i] = cost_list[i-1][1] + min(r[i-1], b[i-1]);
    b[i] = cost_list[i-1][2] + min(r[i-1], g[i-1]);

print(min(r[number], g[number], b[number]));

