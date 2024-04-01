#11048 - 이동하기 (실버2)
from sys import stdin as s
#제출 시 주석 필수
s=open("input.txt","rt")

[n,m] = list(map(int, s.readline().split(' ')));

array=[[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    array[i] = list(map(int, s.readline().split(' '))) 

for i in range(n):
    for j in range(m):
        if (i ==0 and j==0):
            continue;
        elif (i==0 and j >0):
            array[i][j] +=array[i][j-1];
        elif (j==0 and i >0):
            array[i][j] += array[i-1][j];
        else:
            num = max(array[i-1][j], array[i][j-1]);
            num = max(num , array[i-1][j-1])
            array[i][j] += num;
print(array[n-1][m-1])
            
                
