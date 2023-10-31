# 프로그래머스 - 여행경로 (Lv3)
def solution(tickets):
    answer = [];
    visited = [False] * len(tickets);
    
    def dfs(airport, path):
        if (len(path) == len(tickets)+1):
            answer.append(path)
            return # 종료
        for idx, ticket in enumerate(tickets):
            if airport == ticket[0] and visited[idx] == False:
                #인자로 들어온 airport가 출발지 이고 방문하지 않은 경우
                visited[idx] = True;
                dfs(ticket[1], path+[ticket[1]]); #도착지를 airport로 재귀
                visited[idx] = False; # 다른 경로 재탐색을 위해 다시 초기화
        
    #start
    dfs('ICN', ['ICN'])
    #가능한 여러 경로 중 알파벳순으로 맨 앞에 정렬되는 경로가 답
    answer.sort();
    return answer[0]