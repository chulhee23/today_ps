from collections import deque

n, m, k = map(int, input().split())
arr = list(["."] * m for _ in range(n))
for i in range(k):
    x, y = map(int, input().split())
    arr[x-1][y-1] = "#"
# settings

visited = [[False] * m for _ in range(n)]

queue = deque()
ans = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        size = 0
        if arr[i][j] == ".":
            continue

        if visited[i][j] == False:
            visited[i][j] = True
            size += 1
            queue.append((i, j))

            while queue:
                x, y = queue.popleft()

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0<= nx < n and 0<= ny < m and visited[nx][ny] == False:
                        visited[nx][ny] = True
                        if arr[nx][ny] == "#":
                            size += 1
                            queue.append((nx, ny))

            ans = max(ans, size)
print(ans)