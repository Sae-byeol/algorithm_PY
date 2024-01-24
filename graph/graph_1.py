from collections import deque;
#모든 노드의 최단거리 탐색 필요 - bfs가 효율적
def solution(n, edge):
    graph=[[] for _ in range(n+1)];
    answer_arr=[0 for _ in range(n+1)];
    visited =[0 for _ in range(n+1)];
    queue = deque();
    #무방향 그래프 생성
    for e in edge:
        graph[e[0]].append(e[1]);
        graph[e[1]].append(e[0]);
    visited[1] = 1;
    #start
    for i in graph[1]:
        queue.append([i,1]);
        visited[i] = 1;
    while queue:
        [cur_point, cur_count] = queue.popleft();
        answer_arr[cur_point] = cur_count;
        for i in graph[cur_point]:
            if (visited[i] == 0):
                queue.append([i, cur_count+1]);
                visited[i] = 1;
    max_cnt = max(answer_arr);
    answer = answer_arr.count(max_cnt)
    return answer