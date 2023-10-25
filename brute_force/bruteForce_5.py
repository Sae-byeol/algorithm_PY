# 프로그래머스 - 피로도
import itertools;

def solution(k, dungeons):
    answer = -1
    max_arr=[]
    
    index_arr=[]
    num =k;
    for i in range(0, len(dungeons)):
        index_arr.append(i);
    p= list(itertools.permutations(index_arr, len(dungeons)))
    for i in p:
        num =k;
        count =0;
        for j in range(0, len(dungeons)):
            # A,B,C 각각에 대하여
            index= i[j]
            if (num >= dungeons[index][0]):
                num=num-dungeons[index][1];
                count +=1;
        if(count == len(dungeons)):
            return count
        max_arr.append(count);
    answer=max(max_arr);
    return answer