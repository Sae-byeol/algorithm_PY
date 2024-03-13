# 16189 - 에너지 모으기 (실버1)
from sys import stdin as s
import copy

#제출 시 주석 필수
s=open("input.txt","rt") 

def dfs(arr, i, n):
    global ans;

    #i 삭제하고 양쪽 곱하기
    del arr[i];
    n +=  arr[i-1]* arr[i];
    if (len(arr) == 2):
        ans=max(ans, n)
        return;
    for j in range(1, len(arr)-1):
        copy_arr = copy.deepcopy(arr);
        dfs(copy_arr, j, n);
    
ans =0;  
n= int(s.readline());
input_arr=list(map(int, s.readline().split(' ')))

for i in range(1, len(input_arr) -1 ):
    arr = copy.deepcopy(input_arr);
    dfs(arr, i, 0);
print(ans)
    