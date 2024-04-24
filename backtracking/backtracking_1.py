#프로그래머스 - N-Queen (Lv3)
def dfs(col,n,i):
    cnt = 0
    if n == i:
        return 1
    for j in range(n):
        col[i] = j
        for x in range(i):
            if col[x] == col[i]:
                break
            if abs(col[x] - col[i]) == (i-x):
                break
        else:
            cnt += dfs(col, n, i+1)
    return cnt

def solution(n):
    ans = dfs([0]*n, n, 0)
    return ans