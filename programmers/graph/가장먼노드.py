from collections import deque

def solution(n, edge):
    visited = [False] * (n+1)
    queue = deque()
    queue.append((1, 0))
    visited[1] = True
    m = 0
    last_nodes = 1
    while queue:
        cur, lv = queue.popleft()
        if lv != m:
            last_nodes = 1
            m = lv
        elif m != 0:
            last_nodes += 1
        for e in edge:
            if e[0] == cur and visited[e[1]] == False:
                nx = e[1]
                visited[nx] = True
                queue.append((nx, lv + 1))
            elif e[1] == cur and visited[e[0]] == False:
                nx = e[0]
                visited[nx] = True
                queue.append((nx, lv + 1))

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
            m = max(lv, m)

        elif m != 0:
            m_nodes+=1

        info = graph[cur]
        for i in range(len(info)):
            if info[i] == 1 and visited[i] == False:
                visited[i] = True

                queue.append((i, lv + 1))

    return m_nodes


print(solution2(	6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
