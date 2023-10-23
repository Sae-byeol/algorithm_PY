# 2305 - 자리배치
from sys import stdin as s

#제출 시 주석 필수
s=open("input.txt","rt") #절대 경로도 되고, 상대 경로도 된다. # r read t text 
                        
number=int(s.readline());
empty_number=int(s.readline());

dp = [[0 for _ in range(number+1)] for _ in range(number+1)];

dp[3][1]=6;
dp[3][2]=3;
dp[3][3]=6;

for i in range(3, number):
    for j in range(1, i+1):
        if j == 1 | j== i: 
            #모서리
            dp[i][j]=dp[i-1][1];
    
        

print(dp);