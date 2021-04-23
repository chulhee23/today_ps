# 그래프
# bfs
# 시간 초과 주의
# 그래프에선, 간선 리스트 전부 반복하지 말고, dict 과 set 적절히 사용하여 반복을 줄이자.
# 인접 리스트 혹은 인접 행렬 사용할 것

# 상대적으로 인접리스트는 Node의 추가, 삭제가 빈번하게 발생하는 경우 사용하는 것이 좋습니다.
# 간선이 많으면 인접 리스트 길어짐

# 상대적으로 인접행렬은 Edge의 추가, 삭제가 빈번하게 발생하는 경우 사용하는 것이 좋습니다.
# 행렬은 n 개만큼 돌게 됨

from collections import deque

def solution(n, edge):
    visited = [False] * (n+1)
    queue = deque()
    queue.append((1, 0))
    visited[1] = True
    m = 0
    last_nodes = 1

    edges = dict()
    for e in edge:
        if e[0] in edges.keys():
            edges[e[0]].add(e[1])
        else:
            edges[e[0]] = set()
            edges[e[0]].add(e[1])

        if e[1] in edges.keys():
            edges[e[1]].add(e[0])
        else:
            edges[e[1]] = set()
            edges[e[1]].add(e[0])


    while queue:
        cur, lv = queue.popleft()
        if lv != m:
            last_nodes = 1
            m = lv
        elif m != 0:
            last_nodes += 1

        for nx in edges[cur]:
            if visited[nx] == False:
                visited[nx] = True
                queue.append((nx, lv+1))
    return last_nodes



print(solution(	6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))


def solution2(n, vertex):
    graph = [[0] * n for _ in range(n)]
    visited = [False] * n
    for arr in vertex:
        i = arr[0] - 1
        j = arr[1] - 1
        graph[i][j] = 1
        graph[j][i] = 1
    queue = deque()
    queue.append((0, 0))
    visited[0] = True
    m = 0
    m_nodes = 0
    while queue:
        cur, lv = queue.popleft()

        if lv != m:
            m_nodes = 1
            m = lv

        elif m != 0:
            m_nodes+=1

        info = graph[cur]
        for i in range(len(info)):
            if info[i] == 1 and visited[i] == False:
                visited[i] = True
                queue.append((i, lv + 1))

    return m_nodes


print(solution2(	6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
