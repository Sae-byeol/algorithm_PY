#11052 - 카드 구매하기
from sys import stdin as s

#제출 시 주석 필수
s=open("input.txt","rt") #절대 경로도 되고, 상대 경로도 된다.
                         # r read t text 
n=int(s.readline())
number_list = list(map(int, s.readline().split(' ')));
dp=[0 for i in range(0,n)];

for i in range(0,n):
    if (i ==0) : dp[i] = number_list[i]
    else:
        maxNumber = 0;
        for j in range(0,i):
            if (maxNumber <= number_list[i-j-1] + dp[j]): 
                maxNumber = number_list[i-j-1] + dp[j];
        dp[i] = max(maxNumber, number_list[i])

print(dp[n-1]);