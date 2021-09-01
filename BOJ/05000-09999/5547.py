from collections import deque
import sys
input = sys.stdin.readline

w, h = map(int, input().split())
arr = []
visited = [[False] * w for _ in range(h)]

for i in range(h):
    arr.append(list(map(int, input().split())))

mv_1 = [(0, 1), (1, 1), (1, 0), (0, -1), (-1, 0), (-1, 1)]
mv_2 = [(0, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)]

def cur_move(x):
    if x % 2 == 0:
        return mv_1
    else:
        return mv_2

walls = 0
queue = deque()

# for i in range(h):
#     for j in range(w):
#         result = False
#         cur = arr[i][j]
#         if cur == 0 and visited[i][j] == False:
            



for i in range(h):
    for j in range(w):
        cur = arr[i][j]
        


        # 벽 쌓기
        if cur == 1 and visited[i][j] == False:
            queue.append((i, j))
            print(i , j)
            visited[i][j] = True
            while queue:
                count = 0

                x, y = queue.popleft()
                for dx, dy in cur_move(x):
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < h and 0 <= ny < w:
                        if arr[nx][ny] == 1:
                            count += 1
                            if visited[nx][ny] == False:
                                visited[nx][ny] = True
                                queue.append((nx, ny))

                print(y + 1, x + 1, 6 - count)
                walls += 6 - count 

        
print(walls)
