# 9461 - 파도반 수열
from sys import stdin as s

#제출 시 주석 필수
s=open("input.txt","rt") #절대 경로도 되고, 상대 경로도 된다. # r read t text 
                        
number=int(s.readline());
n_list = list();

for i in range(0,number):
    n_list.append(int(s.readline()));

dp=[0]*(101);

dp[1]=1;
dp[2]=1;
dp[3]=1;
dp[4]=2;
dp[5]=2;

for i in range(6,101):
    dp[i]= dp[i-1]+dp[i-5];

for i in n_list:
    print(dp[i]);
