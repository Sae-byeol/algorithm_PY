#20437 - 문자열게임2 (골드5)
from sys import stdin as s
from collections import defaultdict
#제출 시 주석 필수
s=open("input.txt","rt")

k = int(s.readline());
for i in range(0,k):
    #문자열(s.readline().strip())을 배열로 가공해서 사용할 필요 없음(<- 이전 시간초과의 이유)
    #문자열 그대로 배열 다루듯 사용하면 됨. 
    array = s.readline().strip();
    num = int(s.readline());
    if (num == 1): 
        print(1,1);
        continue;
    able_arr_dict=defaultdict(list);
    for i in range(0, len(array)):
        if array.count(array[i]) >= num:
            able_arr_dict[array[i]].append(i)

    if (able_arr_dict): 
        min_answer = len(array);
        max_answer = 0;
    
        for a in able_arr_dict:
            arr=able_arr_dict[a];
            for i in range(0, len(arr) - num + 1):
                ans = arr[i+num-1] - arr[i]+1;
                if ans < min_answer: 
                    min_answer= ans;
                if ans > max_answer:
                    max_answer = ans;
        print(min_answer, max_answer);
    else: 
        print(-1);