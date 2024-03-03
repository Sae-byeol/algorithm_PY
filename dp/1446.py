#1446 - 지름길 (실버1)
from sys import stdin as s

#제출 시 주석 필수
s=open("input.txt","rt") 

[n,d] = list(map(int, s.readline().split(' ')));

input_arr=[[0,0,0] for _ in range(n)];

for i in range(n):
    input_arr[i] = list(map(int, s.readline().split(' ')));

min_arr=[0 for _ in range(d+1)];

for i in range(d+1):
    min_arr[i] = i;
    
for i in range(d+1):
    if ( i > 0):
        min_arr[i] = min(min_arr[i], min_arr[i-1]+1)
    #지름길 있는 경우
    for short in input_arr:
        [start,end,distance] = short;
        if (i == start and end <= d):
            #지름길 적용값과 기존 값 중 작은 값으로 적용
            min_arr[end] = min(min_arr[i]+distance, min_arr[end]);

print(min_arr[d])

