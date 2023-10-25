# 프로그래머스 - 카펫
def solution(brown, yellow):
    answer = []
    n1 = (brown - 4) / 2
    
    # yellow의 약수 구하기
    for i in range(1, yellow+1):
        if (yellow % i ==0):
            num = yellow / i;
            if (i + num == n1):
                answer.append(i+2);
                answer.append(num+2);
                break;
                
    answer.sort(reverse = True);
    
    return answer