# 1932 - 정수 삼각형
from sys import stdin as s

#제출 시 주석 필수
s=open("input.txt","rt") #절대 경로도 되고, 상대 경로도 된다. # r read t text 
number=int(s.readline());

number_list = [[0 for _ in range (0, number)] for _ in range(0,number)];
dp=[[0 for _ in range (0, number)] for _ in range(0,number)];

for i in range(0, number):
    number_list[i] = list(map(int, s.readline().split(' ')));


for i in range(0, number):
    for j in range(0, i+1):
        if (j== 0 ):
            dp[i][j] = dp[i-1][0]+ number_list[i][j];
        elif (j ==i):
            dp[i][j] = dp[i-1][j-1]+ number_list[i][j];
        else: 
            dp[i][j] = max(dp[i-1][j-1] , dp[i-1][j])+ number_list[i][j];

print(max( dp[number -1 ]));
    
