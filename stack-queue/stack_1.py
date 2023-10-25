# 프로그래머스 - 같은 숫자는 싫어
def solution(arr):
    answer = []
    stack =[]
    stack.append(arr[0]);
    
    for i in range(1, len(arr)):
        cur = stack.pop();
        if (cur == arr[i]):
            stack.append(arr[i]);
        else: 
            stack.append(cur);
            stack.append(arr[i])
    answer= stack;
    return answer