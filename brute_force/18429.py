# 18429 - 근손실(실버3)
from sys import stdin as s
import itertools
#제출 시 주석 필수
s=open("input.txt","rt") 

[n,k] = list(map(int, s.readline().split(' ')));
num_list = list(map(int, s.readline().split(' ')));

permutations = list(itertools.permutations(num_list, n));

cnt =0;
for p in permutations:
    val = 500;
    able = True;
    for i in p:
        if (val + i - k < 500):
            able = False;
            break;
        else: 
            val = val + i - k;
    if (able == True):
        cnt+=1;
print(cnt)