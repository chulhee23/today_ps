# 그래프
# BFS

from collections import deque

n = int(input())

# 붙어있는 숫자 처리 12345 -> 1 2 3 4 5
arr = list(list(map(int, map(int, input()))) for _ in range(n))


visited = list([False] * n for _ in range(n))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
ans = []

for i in range(n):
    for j in range(n):
        if visited[i][j] == False and arr[i][j] == 1:
            queue.append((i, j))
            visited[i][j] = True
            count = 1

            while queue:
                x, y = queue.popleft()
                
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False and arr[nx][ny] == 1:
                        queue.append((nx, ny))
                        visited[nx][ny] = True
                        count += 1

            ans.append(count)

        else:
            continue
ans.sort()
print(len(ans))
for num in ans:
    print(num)
