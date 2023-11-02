# 프로그래머스 - 등굣길 (Lv3)
def solution(m, n, puddles):
    answer = 0
    dp= [[0 for _ in range(n+1)] for _ in range(m+1)];
    
    def check(x, y):
        if ([x, y] in puddles):
            return False;
        return True;

    for i in range(1, m+1):
        for j in range(1, n+1 ):
            if (i == 1 and j ==1):
                dp[i][j] =1; # dp[1][1] = 1;
            else:
                left=0;
                top=0;
                #left에서 오는거 가능한지 
                if (i-1 >= 1 and check(i-1, j)):
                    # 범위 벗어나지 않고 웅덩이 아니면 가능
                    left =dp[i-1][j];
                #top에서 오는거 가능한지
                if (j-1 >=1 and check(i, j-1)):
                    top=dp[i][j-1];
                dp[i][j] = left+ top;
                
    answer = dp[i][j] %  1000000007
    return answer