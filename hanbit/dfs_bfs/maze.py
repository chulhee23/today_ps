# 미로 탈출
# 미로 경로에서 최소 경로를 찾아주세요
# bfs 사용.
# visited 라는 개념. 다양한 방법으로 구현될 수 있다.
from collections import deque

# 상하좌우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# visited => 방문한 노드는 해당 노드까지의 거리로 구현. 초기값 : 1.
def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        print(f'x: {x}, y: {y}')
        # 현재 위치에서 4가지 방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            print(f'nx: {nx}, ny: {ny}')
            # 공간 벗어날 때 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 공간 벽
            print(f'graph[nx][ny]: {graph[nx][ny]}')
            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                # bfs. queue 에 append
                queue.append((nx, ny))
    
    # queue empty -> 우측 하단 도착
    return graph[n-1][m-1]


n, m = map(int, input().split())


graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

print(bfs(0,0))
