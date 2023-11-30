# 2559 - 수열(실버3)
from sys import stdin as s
#제출 시 주석 필수
s=open("input.txt","rt")

[num , cnt] =list(map(int, s.readline().split(' ')));

number_list = list(map(int, s.readline().split(' ')));

#누적합 알고리즘 사용

#prefix_sum 배열 만들기
prefix_sum=[0] * num;
prefix_sum[0] = number_list[0];

for i in range(1, num):
    prefix_sum[i] = prefix_sum[i-1] + number_list[i]

sum_arr =[];

start_i = num-1;
while(1):
    end_i = start_i - cnt;
    if (end_i == -1):
        pre_end=0;
        sum_arr.append(prefix_sum[start_i] - pre_end);
        break;
    else: 
        pre_end = prefix_sum[end_i];
        sum_arr.append(prefix_sum[start_i] - pre_end);
    start_i =start_i-1;

print(max(sum_arr))
