import math

def solution(progresses, speeds):
    works = []
    answer = []

    # 실제 작업 날짜를 만들어줍니다.
    for progress, speed in zip(progresses, speeds):
        time = math.ceil((100 - progress) / speed)
        works.append(time)
    
    max_work = works[0]
    days = 0
    
    for idx, work_time in enumerate(works):
        # 아직 도달 못함
        if max_work < work_time:
            answer.append(days)
            days = 1
            max_work = work_time
        else:
            days += 1
        
        # 남은 날짜 처리
        if idx == len(works) - 1:
            answer.append(days) 

    return answer




print(solution([93, 30, 55], [1, 30, 5]))
# 2, 1
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
# 1, 3, 2
