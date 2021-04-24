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


def bfs():
    global ans
    # 새로운 Arr 를 만들어줘야함
    # 2, virus를 퍼뜨릴 예정
    graph = copy.deepcopy(arr)
    queue = copy.deepcopy(virus)
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    queue.append((nx, ny))
    
    tmp = 0
    for tmp_row in graph:
        tmp += tmp_row.count(0)
    ans = max(ans, tmp)


def wall(count):
    if count == 3:
        # 벽 3개 세움
        bfs()
        return
    # 전체 판의 크기 자체가 작다? -> 완전 탐색 가능성 농후
    # DFS 원상태로 돌려놓는 부분을 신경쓰고 기억하자.
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(count + 1)
                arr[i][j] = 0


wall(0)
print(ans)
