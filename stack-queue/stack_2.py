# 프로그래머스 - 올바른 괄호
def solution(s):
    answer = False
    s_list = list(s);
    stck =[];
    if s[0] == ')': return False;
    for i in s_list:
        if i == '(' :
            stck.append(i)
        if i ==')':
            if len(stck) ==0:
                return False;
            stck.pop();
            
    if(len(stck) == 0):
        answer=True;
        
    return answer