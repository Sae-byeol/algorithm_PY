# 프로그래머스 - 최소 직사각형
def solution(sizes):
    answer = 0
    long=[]
    short=[]
    for i in sizes :
        i.sort();
        short.append(i[0]);
        long.append(i[1]);
    short.sort(reverse=True);
    long.sort(reverse=True);
    answer= short[0]*long[0]
    return answer 