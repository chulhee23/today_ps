from collections import deque


def solution(priorities, location):
    location_value = priorities[location]
    print(priorities)
    pri = list(map(list, zip(range(len(priorities)), priorities)))
    print(pri)
    
    arr = []
    queue = deque(pri)

    while queue:
        tmp = queue.popleft()
        
        v = tmp[1]

        if len(queue) == 0:
            arr.append(tmp)
            break

        if tmp[1] >= max(map(lambda x: x[1], queue)):
            arr.append(tmp)
            
        else:
            queue.append(tmp)
    
    
    
    return arr.index([location, location_value]) + 1


print(solution([2, 1, 3, 2], 2))
print("========")
print(solution([1, 1, 9, 1, 1, 1], 0))
