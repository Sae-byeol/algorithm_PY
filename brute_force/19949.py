#19949 - 영재의 시험(실버2)
from sys import stdin as s

#제출 시 주석 필수
s=open("input.txt","rt") 

def dfs(depth):
    global cnt;
    if (depth == 10):
        #answer_arr 다 참 => 정답 체크
        num=0;
        for i in range(10):
            if (answer_arr[i] == input_arr[i]):
                num+=1;
        if (num >= 5):
            cnt+=1;
        return;
    else:
        #answer_arr 채우기
        for i in range(1,6):
            #답은 1,2,3,4,5 중 하나
            if (depth >= 2 and answer_arr[depth-2] == answer_arr[depth -1] == i):
                #3개 연속 된다면? 불가능이므로 이 i 는 건너뛰기
                continue;
            #답 넣어주기
            answer_arr.append(i);
            dfs(depth+1);
            answer_arr.pop();
       
input_arr=list(map(int, s.readline().split(' ')))
answer_arr=[];
cnt=0;
dfs(0);
print(cnt);