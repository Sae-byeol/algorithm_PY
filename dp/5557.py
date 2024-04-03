# 5557 - 1학년 (골드5)
from sys import stdin as s

#제출 시 주석 필수
s=open("input.txt","rt") 

n=int(s.readline())
input_arr = list(map(int, s.readline().split(' ')))
answer =0;
dp=[[0 for _ in range(21)] for _ in range(n-1)]

dp[0][input_arr[0]] =1;

for i in range(0, n-2):
    for j in range(21):
        #1 찾기
        if (dp[i][j] !=0 ):
            if (j+input_arr[i+1] <=20 and j+input_arr[i+1] >= 0):
                dp[i+1][j+input_arr[i+1]] +=dp[i][j];
            if (j-input_arr[i+1] <=20 and j-input_arr[i+1] >= 0):
                dp[i+1][j-input_arr[i+1]] +=dp[i][j];
answer=dp[n-2][input_arr[n-1]];

print(answer)
