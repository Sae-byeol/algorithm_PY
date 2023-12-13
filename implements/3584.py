# 3584 - 가장 가까운 공통 조상 (골드4)
from sys import stdin as s
#제출 시 주석 필수
s=open("input.txt","rt")

test_num =int(s.readline());

for i in range(0, test_num):
    point_num = int(s.readline());
    graph=[0] *(point_num +1);
    for i in range(0,point_num-1):
        [n1, n2] = list(map(int, s.readline().split(' ')));
        graph[n2]=n1;
    [case1, case2] = list(map(int, s.readline().split(' ')));
    top_node = graph[1:].index(0)+1;
    answer =0;
    if (case1 == case2): answer = case1;
    #case1에서 최상위루트까지의 경로
    root1 = [case1]
    while 1:
        n = graph[case1];
        if (n == 0):
            break;
        root1.append(n);
        case1=n;
    #case2에서 최상위루트까지의 경로
    root2=[case2]
    if (case2 in root1):
        #엣지케이스 처리: case2가 정답인 경우, (n == 0 이 되어버리므로 answer에 값이 들어가지 않게 되어 따로 처리)
        answer = case2;
    else: 
        while 1:
            n = graph[case2];
            if (n == 0):
                break;
            #경로 구하던 중 root1에서와 동일 노드 발견시 더이상 경로 구할 필요없이 정답 출력 후 종료
            if (n in root1):
                answer= n;
                break;
            root2.append(n);
            case2=n;
    print(answer)
    
 