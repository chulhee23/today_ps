'''
전략.
문제를 읽다보니, 2명 제한이라는 것을 확인.
가장 많이 탑승하려면 최대와 최소 값이 짝지어서 탑승이 이뤄진다.

boat 라는 배열을 구현하는 것이 아닌, count 값으로 탑승을 처리하자.
'''

def solution(people, limit):
    # 오름차순 정렬
    people.sort()
    
    count = 0
    
    
    i = 0 # 최소
    l = len(people) - 1 # 최대

    while (i < l):
        # 최소와 최대합이 제한조건 이내
        if people[i] + people[l] <= limit:
            # 2명 탑승 처리.
            i += 1
            l -= 1
        else:
            # 최대인 사람 1명만 탑승 처리.
            l -= 1
        
        count += 1

    # 서로 같은 사람을 가르킬 때 -> 같은 사람. 바로 탑승 처리.
    if i == l:
        count += 1
    # 서로 다른 사람 가르킬 때 -> 이미 탑승 처리된 사람.

    return count