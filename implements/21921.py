# 21921 - 블로그 (실버3) 
# 슬라이딩윈도우 알고리즘
from sys import stdin as s
#제출 시 주석 필수
s=open("input.txt","rt")

[n, window_size] = list(map(int, s.readline().split(' ')));
input_arr =list(map(int, s.readline().split(' ')));

sum_arr=[];
first_sum =0;
for i in range(0,window_size):
    first_sum+=input_arr[i];
sum_arr.append(first_sum);

#교집합이 생기므로 슬라이딩 윈도우 사용하여 효율성 높이기
i=0;
start=0;
end=start+window_size;
while(1):
    if (end == n): break;
    sum = sum_arr[i] - input_arr[start]+ input_arr[end];
    sum_arr.append(sum);
    i+=1;
    start+=1;
    end=start+window_size;

#최대 방문자 수 및 개수 구하기
max_cnt = max(sum_arr);
if (max_cnt == 0): print('SAD');
else: 
    print(max_cnt);
    print(sum_arr.count(max_cnt))

    