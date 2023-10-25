# 프로그래머스 - 기능 개발
import math
from collections import deque
def solution(progresses, speeds):
    answer = []
    days=[]
    for i in range(0, len(progresses)):
        days.append(math.ceil( (100-progresses[i])/ speeds[i]));
    queue = deque();
    
    queue.append(days[0]);
    for i in range(1, len(days)):
        cur = queue.popleft();
        if (cur< days[i]):
            #큐 비우기
            answer.append(len(queue)+1);
            queue.clear();
            queue.append(days[i])
        else:
            queue.appendleft(cur)
            queue.append(days[i])
    answer.append(len(queue));
    return answer