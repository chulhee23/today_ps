from collections import deque

n, m = map(int, input().split())

arr = []
for _ in range(m):
    arr.append(input())

visited = [ [False] * n for _ in range(m)]

answer = [0, 0]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
queue.append((0,0))
for i in range(m):
    for j in range(n):
        count = 0
        if visited[i][j] == False:
            queue.append((i, j))
            while queue:
                x, y = queue.popleft()
                if visited[x][y] == False:
                    visited[x][y] = True
                    count += 1
                else:
                    continue
                # if arr[x][y] == "W":
                    
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or ny < 0 or nx >= m or ny >= n:
                        continue
                    if arr[x][y] == arr[nx][ny]:
                        queue.append((nx, ny))
            ans = count * count
            
            if arr[i][j] == 'W':
                answer[0] += ans
            else:
                answer[1] += ans


print(answer[0], answer[1])
