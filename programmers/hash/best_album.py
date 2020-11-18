from collections import Counter

genres = ["classic", "pop","classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

def solution(genres, plays):
    # 장르 우선 수록, 이후 곡 수록
    answer = []
    genres_dic = {}
    for i, v in enumerate(genres):
        genres_dic




#     for key, value in sorted(genre_count.items(), reverse=True):
#         tmp = []
#         max = 0
#         for i, v in enumerate(plays):
#             if genres[i] == key:
#                 if v > max:
#                     tmp.insert(0, i)
#                 else:
#                     tmp.append(i)
#             else:
#                 continue
#         answer += tmp
        

#     return answer

# solution(genres, plays)
