# 1927 - 최소힙(실버2)
from sys import stdin as s
import heapq
#제출 시 주석 필수
s=open("input.txt","rt") 

k = int(s.readline());

q=[];
for i in range(k):
    num = int(s.readline());
    if (num ==0):
        if (len(q) == 0):
            print(0);
        else:
            print(heapq.heappop(q));
    else:
        heapq.heappush(q, num);
        