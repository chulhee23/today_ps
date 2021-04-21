from collections import deque

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, -1 , 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
def bfs(i, j):
    queue = deque()
    queue.append((i, j, 0))
    visited = [[False] * m for _ in range(n)]
    while queue:
        x, y, time = queue.popleft()
        
        if arr[x][y] == 1:
            return time
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < n and 0<= ny < m:
                if visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx, ny, time + 1))

ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] != 1:
            tmp = bfs(i, j)
            ans = max(ans, tmp)

print(ans)