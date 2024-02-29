# 1182 - 부분수열의 합 (실버2)
from sys import stdin as s
import itertools

#제출 시 주석 필수
s=open("input.txt","rt") 

[k, n] = list(map(int, s.readline().split(' ')));

num_arr = list(map(int, s.readline().split(' ')));

ans = 0;
for i in range(1,k+1):
    if (i == 1):
        ans += num_arr.count(n);
    else:
        arr=list(itertools.combinations(num_arr, i));
        for a in arr:
            if(sum(a) == n):
                ans+=1;

print(ans)