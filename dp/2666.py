# 2666- 벽장문의 이동
from sys import stdin as s

#제출 시 주석 필수
s=open("input.txt","rt") #절대 경로도 되고, 상대 경로도 된다. # r read t text 
                        
total_number=int(s.readline());
empty_list = list(map(int, s.readline().split(' ')));
problem_number = int(s.readline());
problem_list = list();

door_list=[0 for i in range(0, total_number)];
dp = [[[0 for _ in range(total_number+1)] for _ in range(total_number+1)] for _ in range(total_number+1)] #3차원 배열

for i in range(0, problem_number):
    n= int(s.readline());
    problem_list.append(n);

def solve(index, empty1, empty2):
    if index == problem_number: return 0;
    cur = problem_list[index]; #3
    dp[cur][empty1][empty2] = min(
        abs(empty1 - cur) + solve(index+1, cur, empty2) , abs(empty2-cur) + solve(index+1, empty1, cur)
    )
    return dp[cur][empty1][empty2];
    
print(solve(0, empty_list[0], empty_list[1]));
    

        
        
        
        
    

