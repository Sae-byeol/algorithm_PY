# 프로그래머스 - 단어 변환 Lv3
def solution(begin, target, words):
    answer = 0
    visited=[];
    word_length = len(begin)
    cnt_arr=[];
    def dfs(cur, cnt):
        if (cur == target):
            cnt_arr.append(cnt);
            return;
        visited.append(cur);
        for word in words:
            if (word not in visited):
                diff =0;
                for i in range(0,word_length):
                    if (word[i] != cur[i]):
                        diff+=1;
                if(diff ==1):
                    dfs(word, cnt+1);
    #start
    dfs(begin, 0)

    if (len(cnt_arr) == 0):
        answer=0;
    else: 
        answer= min(cnt_arr)
    return answer