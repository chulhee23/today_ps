# from collections import deque


# def dfs(numbers, target, idx, s):
#     global answer
#     N = len(numbers)
#     if(idx == N and target == s):
#         answer += 1
#         return
#     if(idx == N):
#         return
#     dfs(numbers, target, idx + 1,  s + numbers[idx])
#     dfs(numbers, target, idx + 1, s - numbers[idx])

# def solution(numbers, target):
#     global answer
#     answer = 0
#     idx = 0
#     s = 0
#     dfs(numbers, target, idx ,s)    
    
#     return answer

# from itertools import product

# def solution(numbers, target):
#     l = [(x, -x) for x in numbers]
#     print(l)
#     s = list(map(sum, product(*l)))
#     print(product(*l))
#     print(s)
#     return s.count(target)



# numbers = [1, 1, 1, 1, 1]
# target = 3

# print(solution(numbers, target))





# 복습---------
from collections import deque

# bfs 풀이

def solution2(numbers, target):
    queue = deque([0])

    count = 1

    for number in numbers:
        tmp = count
        count *= 2
        while queue and tmp > 0:
            item = queue.popleft()

            queue.append(item + number)
            queue.append(item - number)
            tmp -= 1


    print(list(queue))
    answer = len(list(filter(lambda x: x == target, list(queue))))
    return answer


numbers = [1, 1, 1, 1, 1]
target = 3

print(solution2(numbers, target))












