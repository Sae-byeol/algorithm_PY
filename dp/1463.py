# 1463 1로 만들기
from sys import stdin as s
#제출 시 주석 필수
s=open("input.txt","rt")

number= int(s.readline());

#dp: greedy와 다르게 현재만 생각하면 전체적인 결과값에 맞지 않을 수 있음. '메모이제이션'을 활용하여 이전/이후 값 고려하며 계산

dp=[0]*(number+1) #1까지의 연산 횟수 저장하는 배열

for i in range(2, number+1):
    dp[i] = dp[i-1]+1; #일단 -1 했다고 가정
    if (i % 2 ==0 ):
        dp[i] = min(dp[i], dp[i//2] + 1); # +1은 이전 값에 연산횟수를 +1하는 것
    if (i % 3 ==0):#6의 배수의 경우에는 2로 나눈경우, 3으로 나눈경우 모두 비교 필요
        dp[i] =  min(dp[i], dp[i//3] + 1);
        
print(dp[number]);