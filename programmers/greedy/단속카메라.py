'''
적절한 sort 를 이용하면 풀이 시간을 단축할 수 있습니다.
'''


def solution(routes):
    answer = 1
    routes.sort(key=lambda x: x[0]) # 시작으로 정렬
    start = routes[0][0]
    end = routes[0][1]
    for idx in range(1, len(routes)):
        route = routes[idx]
        if end < route[0]:
            answer += 1
            end = route[1]

        if end > route[1]:
            end = route[1]

        
    return answer


print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))


[[-20, 15], [-18, -13], [-14, -5], [-5, -3]]
