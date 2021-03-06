from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        print(queue)
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
            


graph = [
    [],  # 0번 인덱스 정보. 1번 노드부터 시작
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [1, 7],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [False] * 9

bfs(graph, 1, visited)
