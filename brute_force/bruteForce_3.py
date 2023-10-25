# 프로그래머스 - 소수 찾기
import itertools;

def is_prime(x):    
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    n = list(numbers)

    a = []
    for i in range(1, len(n)+1):
        a+=list(itertools.permutations(n, i))   
    
    b = []
    for i in a:
        b.append(int(''.join(i)))   
        
    b = list(set(b))

    for i in b:
        if i <= 1:
            continue    
        elif is_prime(i):   
            answer += 1  
    return answer;