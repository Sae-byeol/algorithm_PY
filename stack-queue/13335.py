# 13335 - 트럭(실버1)
from sys import stdin as s
from collections import deque

#제출 시 주석 필수
s=open("input.txt","rt")

[n,w,l] = list(map(int, s.readline().split(' ')));
num_list = list(map(int , s.readline().split(' ')));

#빈 공간은 0으로 채워둬야 트럭 append할때 뒤에서부터 한 칸씩 이동 가능
bridge =deque([0] * w)
truck_index=0;
count = 0;
while(1):
    if(truck_index == len(num_list)):
        count+=w;
        break;
    bridge.popleft();
    bridge_weight = sum(bridge);
    if(bridge_weight + num_list[truck_index] <= l):
        #push 가능
        bridge.append(num_list[truck_index]);
        truck_index+=1;
    else:
        bridge.append(0);
    count+=1;

print(count);
