# BFS DFS 완전탐색
# 원상태로 돌리면서 돌아와!
# copy
from collections import deque
import copy
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())

ans = 0

arr = []

virus = deque()
for i in range(n):
    tmp = list(map(int, input().split()))
    for x in range(m):
        if tmp[x] == 2:
            virus.append((i, x))
    arr.append(tmp)


# 벽 세워
# 3개 어떻게?
# i j k 로 돌려?
def bfs():
    global ans
    graph = copy.deepcopy(arr)
    queue  = copy.deepcopy(virus)

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    queue.append((nx, ny))

    # 0 개수 세기
    tmp = 0
    for tmp_row in graph:
        tmp += tmp_row.count(0)
    ans = max(ans, tmp)


def wall(count):
    if count == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(1)
                arr[i][j] = 0

wall(0)
