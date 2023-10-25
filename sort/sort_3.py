# 프로그래머스 - H-Index
def solution(citations):
    answer = 0
    max_num =max(citations)
    min_num = min(citations)
    for h in range(0, max_num+1):
        count =0;
        for i in citations:
            if (i >= h):
                count+=1;
        if (count >= h):
            answer= h;
    return answer