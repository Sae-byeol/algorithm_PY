# 10826 - 피보나치 수 4
from sys import stdin as s

#제출 시 주석 필수
s=open("input.txt","rt") #절대 경로도 되고, 상대 경로도 된다. # r read t text 
                        
number=int(s.readline());

dp=[0]*(10000+1);

dp[1]=1;

for i in range(2, number+1):
    dp[i] = dp[i-1]+dp[i-2];
    
print(dp[number])