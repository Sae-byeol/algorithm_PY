# 프로그래머스 - 프로세스
from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque();
    answer_array=[];
    for i in range(0, len(priorities)) : 
        queue.append([priorities[i], i]);
    
    while(len(queue) !=0 ):
        cur = queue.popleft();
        max=0;
        for j in range(0, len(queue)):
            #남은 애들 중 max
            if (max < queue[j][0]):
                max=queue[j][0]
        if(max <= cur[0]):
            answer_array.append(cur);
        else:
            queue.append(cur);
    
    location_index = priorities[location];
    answer=answer_array.index([location_index,location])+1;
    
    return answer