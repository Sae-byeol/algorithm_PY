# 프로그래머스 - 광물캐기 (Lv2) 
def solution(picks, minerals):
    answer = 0
    dia_pick, iron_pick, stone_pick = picks #각 곡괭이의 개수
    #각 곡괭이의 피로도
    dia_pick_fatigue = {
        "diamond": 1, 
        "iron": 1,
        "stone": 1
    }
    iron_pick_fatigue ={
        "diamond": 5,
        "iron": 1, 
        "stone": 1
    }
    stone_pick_fatigue={
        "diamond": 25, 
        "iron": 5, 
        "stone": 1
    }
    
    #광물을 5개씩 끊어 이차원 배열로 저장하고, 곡괭이의 개수 초과하는 부분은 자름
    minerals =[minerals[i:i+5] for i in range(0, len(minerals), 5)][:sum(picks)]
    # 이차원 배열 minerals의 각 원소(1치원 배열) 정렬 조건 : 1순위 = 다이아몬드 개수 -> 2순위 = 철 개수 -> 3순위 = 돌 개수
    minerals.sort(key= lambda x: (x.count('diamond'), x.count('iron'), x.count('stone')), reverse=True)
    
    #5개씩 나눈 각 광물 모음에 대해 광물 캐기 시작
    for mineral in minerals:
        #곡괭이 우선 순위: 다이아, 철, 돌
        if (dia_pick > 0):
            for m in mineral:
                answer+=dia_pick_fatigue[m]
            dia_pick -=1
        elif (iron_pick > 0):
            for m in mineral: 
                answer+=iron_pick_fatigue[m]
            iron_pick -=1
        elif (stone_pick > 0):
            for m in mineral:
                answer+=stone_pick_fatigue[m]
            stone_pick -=1            
    
    return answer

print(solution([1, 1, 0], ["stone", "stone", "iron", "stone", "diamond", "diamond", "diamond", "diamond", "diamond", "diamond"]))