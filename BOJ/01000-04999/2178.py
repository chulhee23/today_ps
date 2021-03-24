from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

arr = []
for _ in range(n):
    arr.append(input().rstrip())


visited = [[0] * m for _ in range(n)]
    
queue = deque()
queue.append((0,0,1))
visited[0][0] = True

while queue:
    x, y, c = queue.popleft()
    if x == n-1 and y == m-1:
        print(c)
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if visited[nx][ny] == False and arr[nx][ny] == '1':
            # visited[nx][ny] == False 인 경우에 방문처리해야 시간초과 피할 수 있다.
            visited[nx][ny] = True

            queue.append((nx, ny, c+1))

