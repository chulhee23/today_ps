# 삼성
# BFS
# 아기 상어
import sys
from collections import deque

n = int(input())
arr = []
shark_x = n
shark_y = n

for i in range(n):
    tmp = list(map(int, input().split()))
    if 9 in tmp:
        shark_x = i
        shark_y = tmp.index(9)
    arr.append(tmp)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# size, eat, time
shark = [2, 0, 0]

# update가 되었는지 체크
update = True
while(update):
    # 탐색을 queue로 해도, 전부  업데이트 실패한 경우 
    update = False
    queue = deque()

    visited = [[False] * n for _ in range(n)]
    visited[shark_x][shark_y] = True
    queue.append((shark_x, shark_y, shark[2]))

    candi_x = n
    candi_y = n
    candi_time = -1

    while queue:
        x, y, time = queue.popleft()
        # 아직 후보군 샤크 중 갱신이 되었다면
        # 아래 조건에 걸리면 가까운 물고기는 이미 잡힘.예제 3의 1 도착하는 경우에 해당
        if (candi_time != -1 and candi_time < time):
            break
            # while 문 벗어남
        if (arr[x][y] < shark[0] and arr[x][y] != 0):
            update = True
            if (candi_y > y or (candi_y == y and candi_x > x)):
                candi_y = y
                candi_x = x
                candi_time = time
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            ntime = time + 1
            if 0 <= nx < n and 0<= ny < n:
                if (visited[nx][ny] == False and arr[nx][ny] <= shark[0]):
                    visited[nx][ny] = True
                    queue.append((nx, ny, ntime))

    # 물고기를 먹을 수 있었다
    # 맵 갱신, 상어 갱신
    if (update):
        shark_x = candi_x
        shark_y = candi_y
        shark[2] = candi_time
        
        shark[1] += 1
        if shark[1] == shark[0]:
            shark[0] += 1
            shark[1] = 0
        arr[shark_x][shark_y] = 0

print(shark[2])
# 모두 벗어나면 샤크의 시간 출력