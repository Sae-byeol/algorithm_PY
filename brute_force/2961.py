# 2961 - 도영이가 만든 맛있는 음식(실버2)
from sys import stdin as s

#제출 시 주석 필수
s=open("input.txt","rt") 

def dfs(depth, idx):
    global answer;
    if (depth == num):
        sour , bitter = 1,0;
        #원하는 재료 갯수만큼 다 뽑았으면 => sour, bitter 계산 
        for i in range(n):
            if (visited[i] ==1):
                sour*=input_arr[i][0];
                bitter+=input_arr[i][1];
        answer=min(answer, abs(sour-bitter))
        return;
    for i in range(idx, n):
        visited[i] =1;
        dfs(depth+1, i+1);
        visited[i] =0;

n= int(s.readline());
visited=[0 for _ in range(n)];
input_arr=[[0,0] for _ in range(n)];
answer=1e9;
for i in range(n):
    input_arr[i] = list(map(int, s.readline().split(' ')))

num =0;
for i in range(1, n+1):
    num = i;
    dfs(0,0)

print(answer);