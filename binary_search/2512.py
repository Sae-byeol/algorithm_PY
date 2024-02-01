from sys import stdin as s
import math
#제출 시 주석 필수
s=open("input.txt","rt") 
k= int(s.readline());
num_arr = list(map(int, s.readline().split()));
total_money= int(s.readline());

ans = 0;
start= 1;
end = max(num_arr);

while start<=end:
    mid = (start+end)//2;
    num=0;
    for i in num_arr:
        if (i <= mid):
            num+=i;
        else:
            num+=mid;
    if (num==total_money):
        ans=mid;
        break;
    if (num < total_money):
        start=mid+1;
    else:
        end = mid -1;

if (ans == 0):
    ans = end;
print(ans)
    
        

