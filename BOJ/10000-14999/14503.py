# DP
# 청소 문제
# DFS + DP


import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 북 동 남 서
# 0 1 2 3
rx, ry, d = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(n))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ans = 0



def clean(x, y, d):
    global ans
    if arr[x][y] == 0:
        arr[x][y] = 2
        ans += 1

    for _ in range(4):
        nd = (d + 3) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 0:
                clean(nx, ny, nd)
                # 일종의 DFS 탐색 위해
                return

            d = nd # 그 다음 nd 계산 위해

    # 뒤로 이동
    nx = x - dx[d]
    ny = y - dy[d]

    if 0 <= nx < n and 0 <= ny < m:
        if arr[nx][ny] == 1:
            return 
        clean(nx, ny, d)


clean(rx, ry, d)
print(ans)
