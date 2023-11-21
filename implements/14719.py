# 14719 - 빗물
from sys import stdin as s
#제출 시 주석 필수
s=open("input.txt","rt")

[h, w]=list(map(int, s.readline().split(' ')));
wall_list = list(map(int, s.readline().split(' ')));
answer =0;
for i in range(1, w-1):
    cur = wall_list[i];
    #i 기준 오른쪽의 max, 왼쪽의 max 구하기
    left = max(wall_list[:i]);
    right= max(wall_list[i+1:])
    # 둘 중 작은 값
    small = min(left, right);
    if (small != 0 and small > cur):
        answer= answer+ (small - cur);
print(answer);
        