# 2579 - 계단 오르기
from sys import stdin as s

#제출 시 주석 필수
s=open("input.txt","rt") #절대 경로도 되고, 상대 경로도 된다. # r read t text 
                        
number=int(s.readline());

stair_list = [0] * (300)
for i in range(0,number):
    stair_list[i] = int(s.readline());

dp=[0]*(301);

dp[1]=stair_list[0];
dp[2]=stair_list[0]+stair_list[1]
dp[3]=max(stair_list[2]+stair_list[1] , stair_list[2]+stair_list[0])

for i in range(4, number+1):
    dp[i]= max(dp[i -2]+ stair_list[i -1], dp[i-3]+stair_list[i -1]+stair_list[i -2])


print(dp[number]); 