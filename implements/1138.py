# 1138 - 한 줄로 서기(실버2)
from sys import stdin as s
#제출 시 주석 필수
s=open("input.txt","rt")

k= int(s.readline());
input_arr=list(map(int, s.readline().split(' ')))
answer_arr = [0] * k;

for i in range(0, len(input_arr)):
    height = i+1;
    num = input_arr[i];
    cnt =0;
    for j in range(0, len(answer_arr)):
        if (answer_arr[j] != 0):
            continue;
        if (cnt == num):
            answer_arr[j] = height;
            break;
        cnt+=1;
        
#괄호 없이 배열 출력 하는 법
print(*answer_arr)