# 1522 - 문자열 교환 (골드5)
from sys import stdin as s

#제출 시 주석 필수
s=open("input.txt","rt") 
input_arr =list(map(str, s.readline().strip()));

#슬라이딩 윈도우에서 쓸 윈도우의 크기 = a의 갯수
window_size = input_arr.count('a');
#원형 배열이므로 두개 붙여주기
input_arr+= input_arr;

start = 0;
end= start+window_size;
answer_arr =[];
while(1):
    if (end == len(input_arr)): 
        break;
    sliced_arr = input_arr[start:end];
    switch_cnt = sliced_arr.count('b');
    answer_arr.append(switch_cnt);
    start+=1;
    end=start+window_size;

print(min(answer_arr));