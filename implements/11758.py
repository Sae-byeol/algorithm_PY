#11758 - CCW(골드5)
from sys import stdin as s
#제출 시 주석 필수
s=open("input.txt","rt")

input_arr=[]
for i in range(3):
    input_arr.append(list(map(int, s.readline().split(' '))))

#ccw 알고리즘

#p1, p2 벡터
vertor_1 = [input_arr[1][0] - input_arr[0][0] , input_arr[1][1] - input_arr[0][1]];
#p2, p3 벡터
vertor_2 = [input_arr[2][0] - input_arr[0][0] , input_arr[2][1] - input_arr[0][1]];

# 두 벡터의 곱
num = vertor_1[0] * vertor_2[1] - vertor_1[1] * vertor_2[0]
    
if (num > 0):
    print(1);
elif (num < 0):
    print(-1);
else: print(0)
    