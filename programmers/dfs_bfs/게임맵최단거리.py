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


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def solution(maps):
    answer = 0
    queue = deque()
    queue.append((0, 0, 1))
    visited = [[0] * len(maps[0]) for x in range(len(maps))]
    while queue:
        x, y, answer = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간 벗어나면 무시
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                continue
            
            # 갈 수 없어도 무시
            if maps[nx][ny] == 0:
                continue
            
            if maps[nx][ny] == 1:
                if visited[nx][ny] == 0:
                    queue.append((nx, ny, answer+1))
                    visited[nx][ny] = answer + 1
                else:
                    if visited[nx][ny] > answer + 1:
                        queue.append((nx, ny, answer+1))
                        visited[nx][ny] = answer + 1



    if visited[-1][-1] == 0:
        return -1
    return visited[-1][-1]



print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
