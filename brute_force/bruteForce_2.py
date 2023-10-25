# 프로그래머스 - 모의고사
def solution(answers):
    answer = []
    s1=[1,2,3,4,5,1,2,3,4,5]
    s2=[2,1,2,3,2,4,2,5]
    s3=[3,3,1,1,2,2,4,4,5,5]
    
    cnt1=0;
    cnt2=0;
    cnt3=0;
    for i in range(0, len(answers)):
        index=i%10;
        index2 = i%8;
        if (answers[i] == s1[index]): cnt1+=1;
        if (answers[i] == s2[index2]): cnt2+=1;
        if (answers[i] == s3[index]): cnt3+=1;
        
    maxi=max(cnt1,cnt2, cnt3);
    if(cnt1 == maxi):
        answer.append(1)
    if(cnt2 == maxi):
        answer.append(2);
    if (cnt3 == maxi):
        answer.append(3)
        
    return answer