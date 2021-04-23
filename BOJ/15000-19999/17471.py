# 게리맨더링
from collections import deque
from itertools import combinations
is_update = False
ans = float('inf')
n = int(input())

graph = [ [0] * n for _ in range(n) ]


people = list(map(int, input().split()))


for i in range(n):
    tmp = list(map(int, input().split()))
    # 1: 2 2 4
    # 2개. 2와 4 연결됨
    # index 1 3
    if tmp[0] != 0:
        for j in range(tmp[0]):
            graph[i][tmp[1 + j] - 1] = 1
# initial settings

def is_group(area, graph, goal):
    queue = deque()
    visited = [False] * len(graph)
    visited[area[0]] = True
    queue.append(area[0])
    count = 1
    
    while queue:
        x = queue.popleft()
        node = graph[x]
        for i in range(len(node)):
            if visited[i] == False and node[i] == 1 and i in area:
                visited[i] = True
                count += 1
                queue.append(i)
    if count == goal:
        return True
    else:
        return False

    
for i in range(1, n//2 + 1):
    comb = combinations(range(0, n), i) #tuple () 반환
    for a_area_set in comb:
        a_area = list(set(a_area_set))
        b_area = list(set(range(0, n)) - set(a_area_set)) # 중복 제거에도 쓰이지만 list의 차집합 구할 때도 가능
        
        sum_a = 0
        sum_b = 0
        
        if is_group(a_area, graph, i) == True and is_group(b_area, graph, n - i) == True:
            for v in a_area:
                sum_a += people[v]
            for v in b_area:
                sum_b += people[v]
            is_update = True
            ans = min(ans, abs(sum_a - sum_b))

if is_update:
    print(ans)
else:
    print(-1)