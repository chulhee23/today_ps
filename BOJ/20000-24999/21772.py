# 백트래킹
from collections import deque
import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())
arr = []
dog = ()

visited = [[False] * c for _ in range(r)]

for i in range(r):
    cc = input().rstrip()
    if "G" in cc:
        j = cc.index("G")
        dog = (i, j, 0, 0)
    cc = list(cc)
    arr.append(cc)

dx = [-1, 1, 0, 0, 0]
dy = [0, 0, -1, 1, 0]

ans = 0

def dfs(x, y, cnt, time, limit):
    global ans
    if time == limit:
        ans = max(ans, cnt)
        return ans
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != "#":
            if x == nx and y == ny:
               dfs(nx, ny, cnt, time + 1, limit) 
            else:
                if arr[nx][ny] == "S":
                    arr[nx][ny] = "."
                    dfs(nx, ny, cnt + 1, time + 1, limit)
                    arr[nx][ny] = "S"
                else:
                    dfs(nx, ny, cnt , time+ 1, limit)

                
                
    

dfs(dog[0], dog[1], 0, 0, t)

print(ans)