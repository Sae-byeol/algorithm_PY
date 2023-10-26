# 프로그래머스 - 타겟 넘버
def solution(numbers, target):
    answer = 0
    cnt =0;
    arr=[]
    def dfs(cnt, num, index):
        if(cnt == len(numbers)) :
            arr.append(num);
            return; #종료조건
        #재귀
        dfs(cnt+1, num+numbers[index], index+1)
        dfs(cnt+1, num-numbers[index], index+1)
        
    dfs(0, 0 , 0)
    for i in arr :
        if (i == target):
            answer+=1;
    return answer