# 프로그래머스 - 전화번호 목록
def solution(phone_book):
    answer = True
    phone_book.sort();
    start=phone_book[0];
    for i in range(1, len(phone_book)):
        if (len(phone_book[i]) >= len(start)):
            if (phone_book[i][0:len(start)] == start) :
                return False;
        start= phone_book[i];
    
    return answer