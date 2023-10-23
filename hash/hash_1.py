# 프로그래머스 - 폰켓몬
def solution(nums):
    answer = 0;
    number = len(nums) / 2 ;
    #중복 제거
    array= list(set(nums));

    if (number < len(array)): 
        answer= number;
    else: answer = len(array);
    
    return answer