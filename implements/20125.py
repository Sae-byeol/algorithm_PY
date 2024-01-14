# 20125 - 쿠키의 신체 측정(실버4)
from sys import stdin as s

#제출 시 주석 필수
s=open("input.txt","rt")

k=int(s.readline());
arr = [[0 for _ in range(k)] for _ in range(k)];

for i in range(k):
    str= s.readline();
    for j in range(k):
        arr[i][j]= str[j];

def find(start_x, start_y,type):
    x=start_x;
    y=start_y;
    cnt=0;
    while(1):
        if (x >= k or y >=k or x < 0 or y < 0 or arr[x][y] == '_'):
            break;
        if (arr[x][y] == '*'):
            cnt+=1;  
        if (type == 'left_arm'):
            y-=1;
        if (type == 'right_arm'):
            y+=1;
        if (type== 'waist' or type=='left_leg' or type == 'right_leg'):
            x+=1;
    return cnt;

heart =[0,0]
for i in range(k):
    for j in range(k):
        if (arr[i][j] == '*' and heart==[0,0]):
            heart=[i+1, j];
answer_arr =[];
answer_arr.append(find(heart[0], heart[1]-1, 'left_arm'));
answer_arr.append(find(heart[0], heart[1]+1, 'right_arm'));
answer_arr.append(find(heart[0]+1, heart[1], 'waist'));
answer_arr.append(find(heart[0]+1+answer_arr[2], heart[1]-1, 'left_leg'));
answer_arr.append(find(heart[0]+1+answer_arr[2], heart[1]+1, 'right_leg'));

print(heart[0]+1, heart[1]+1)
print(*answer_arr)