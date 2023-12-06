# 1027 - 고층건물 (골드4)
from sys import stdin as s

#제출 시 주석 필수
s=open("input.txt","rt")

k= int(s.readline());
input_arr= list(map(int, s.readline().split(' ')));
dp = [0] * k;
for i in range(0, k):
    left_cnt=0;
    right_cnt=0;
    if (i != k-1):
        #오른쪽
        right_max=0;
        for j in range(i+1, k):
            right = (input_arr[j] - input_arr[i]) / (j-i);
            if (j == i+1): 
                right_max = right;
                right_cnt=1;
            else: 
                if (right > right_max):
                    right_max = right;
                    right_cnt+=1;
    if (i != 0):
        #왼쪽
        left_min=0;
        #for문 거꾸로(큰 수에서 작은수로) 돌리는 법은 range의 3번째 인수로 -1 주기. 
        for p in range(i-1, -1, -1):
            left = (input_arr[i] - input_arr[p]) / (i-p);
            if (p == i-1):
                left_min= left;
                left_cnt=1;
            else:
                if (left < left_min):
                    left_min = left;
                    left_cnt+=1;
                    
    dp[i] = left_cnt+right_cnt;
print(max(dp))
