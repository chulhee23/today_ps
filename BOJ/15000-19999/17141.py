from itertools import combinations
from collections import deque
import sys
import copy
input = sys.stdin.readline

n, m = map(int, input().split())

original_arr = []
virus = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    tmp = list(map(int, input().split()))
    original_arr.append(tmp)

    for j in range(len(tmp)):
        if tmp[j] == 2:
            virus.append((i, j, 0))


v_cases = combinations(virus, m)

ans = n * n

for v_case in v_cases:
    # 모든 경우에 대해서, 
    arr = copy.deepcopy(original_arr)
    queue = deque()
    
    visited = [[False] * n for _ in range(n)]
    times = 0
    flag = True

    for viruses in v_case:
        visited[viruses[0]][viruses[1]] = True
        queue.append(viruses)

    while queue:
        cx, cy, ct = queue.popleft()
        times = max(times, ct)
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
                if arr[nx][ny] == 0 or arr[nx][ny] == 2:
                    visited[nx][ny] = True
                    arr[nx][ny] = 1
                    queue.append((nx, ny, ct + 1))

    # is full?
    for row in arr:
        if 0 in row:
            flag = False
            break
        
    if flag:
        ans = min(ans, times)

if ans == n * n:
    print(-1)
else:
    print(ans)
