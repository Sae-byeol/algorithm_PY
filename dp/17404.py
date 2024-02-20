#17404 - RGB거리2 (골드4)
from sys import stdin as s

#제출 시 주석 필수
s=open("input.txt","rt")

n = int(s.readline());
input_arr = [[0,0,0] for _ in range(n)]

for i in range(n):
    input_arr[i] = list(map(int, s.readline().split(' ')))

ans =0;    
# 첫 집이 R
r=[0 for _ in range(n+1)]
g=[0 for _ in range(n+1)]
b=[0 for _ in range(n+1)]

r[1] = input_arr[0][0];
g[1] = float('inf');
b[1] = float('inf');
for i in range(2, n+1):
    if (i != 2):
        r[i] = input_arr[i-1][0] + min(g[i-1], b[i-1]);
        g[i] = input_arr[i-1][1] + min(r[i-1], b[i-1]);
        b[i] = input_arr[i-1][2] + min(g[i-1], r[i-1]);
    else:
        r[i]=float('inf');
        g[i] = input_arr[i-1][1] + min(r[i-1], b[i-1]);
        b[i] = input_arr[i-1][2] + min(g[i-1], r[i-1]);
ans = min(g[n], b[n]);

# 첫 집이 G
r=[0 for _ in range(n+1)]
g=[0 for _ in range(n+1)]
b=[0 for _ in range(n+1)]

r[1] = float('inf');
g[1] = input_arr[0][1];
b[1] = float('inf');
for i in range(2, n+1):
    if (i != 2):
        r[i] = input_arr[i-1][0] + min(g[i-1], b[i-1]);
        g[i] = input_arr[i-1][1] + min(r[i-1], b[i-1]);
        b[i] = input_arr[i-1][2] + min(g[i-1], r[i-1]);
    else:
        g[i]=float('inf');
        r[i] = input_arr[i-1][0] + min(g[i-1], b[i-1]);
        b[i] = input_arr[i-1][2] + min(g[i-1], r[i-1]);
temp = min(r[n], b[n]);
ans = min(ans, temp)

# 첫 집이 B
r=[0 for _ in range(n+1)]
g=[0 for _ in range(n+1)]
b=[0 for _ in range(n+1)]

r[1] = float('inf');
g[1] = float('inf');
b[1] = input_arr[0][2]
for i in range(2, n+1):
    if (i != 2):
        r[i] = input_arr[i-1][0] + min(g[i-1], b[i-1]);
        g[i] = input_arr[i-1][1] + min(r[i-1], b[i-1]);
        b[i] = input_arr[i-1][2] + min(g[i-1], r[i-1]);
    else:
        b[i]=float('inf');
        r[i] = input_arr[i-1][0] + min(g[i-1], b[i-1]);
        g[i] = input_arr[i-1][1] + min(b[i-1], r[i-1]);
temp = min(g[n], r[n]);
ans = min(ans, temp)
print(ans)