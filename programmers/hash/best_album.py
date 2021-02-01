from collections import Counter

genres = ["classic", "pop","classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

def solution(genres, plays):
    # 장르 우선 수록, 이후 곡 수록
    dic = {}
    for v in (genres):
        dic[v] = []
        
    for i, v in enumerate(genres):
        dic[v].append([i, plays[i]])

    print(dic)

    for k, v in enumerate(dic):
        
        



solution(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500])
# ['classic', 'pop', 'classic', 'classic', 'pop']
# [500, 600, 150, 800, 2500]
# [4, 1, 3, 0]

'''
전략.
1. 우선 장르별 합산 
2. 장르 내에서 많이 들은 2곡 선정
많이들은 장르 1, 2위 곡
2번째 장릉 1, 2위 곡
'''
