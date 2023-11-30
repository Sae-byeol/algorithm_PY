# 2차원 배열의 합 - 실버5
from sys import stdin as s
#제출 시 주석 필수
s=open("input.txt","rt")

[n , m] =list(map(int, s.readline().split(' ')));
arr = [[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(n):
    num_list = list(map(int, s.readline().split(' ')));
    for j in range(m):
        arr[i+1][j+1] = num_list[j]
        
k = int(s.readline());
input_list = [];
for i in range(k):
    input_list.append(list(map(int, s.readline().split(' '))));
    
#prefix_sum 배열 생성
prefix_sum =  [[0 for _ in range(m+1)] for _ in range(n+1)];
for i in range(n):
    for j in range(m):
        prefix_sum[i+1][j+1] = prefix_sum[i+1][j] + prefix_sum[i][j+1] + arr[i+1][j+1] - prefix_sum[i][j];

#정답 출력
for arr in input_list:
   [i,j,x,y] = arr;
   print(prefix_sum[x][y] - prefix_sum[x][j-1] - prefix_sum[i-1][y] + prefix_sum[i-1][j-1])

    