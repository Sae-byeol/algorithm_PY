# 소프티어 - 지도 자동 구축 (Lv2)
import sys
std = sys.stdin;

n = int(std.readline());
dp=[0] * (n+1);
num =2;
for i in range(0,n+1):
  dp[i] = num*num;
  num = num+(num - 1);
print(dp[n])