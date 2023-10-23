# 프로그래머스 - 의상
def solution(clothes):
    answer = 1
    clothes_dict = dict();
    clothes.sort(key = lambda x: x[1]);
    
    for clothe, type in clothes:
        clothes_dict[type] = clothes_dict.get(type, 0) +1;
    
    values = list(clothes_dict.values())
    
    for i in values:
        answer *= (i+1)
    
    answer-=1;
        
    return answer