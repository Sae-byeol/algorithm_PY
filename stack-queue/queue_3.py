# 프로그래머스 - 주식 가격
def solution(prices):
    answer = []
    for i in range(0, len(prices)):
        cur = prices[i];
        count =0;
        for j in range(i+1, len(prices)):
            if(cur <= prices[j]):
                count+=1;
            else:
                count+=1;
                break;
        answer.append(count);
        
    return answer