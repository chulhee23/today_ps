# 테트로미노
# DFS
# 삼성
# 브루트 포스
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * m for _ in range(n)]

ans = 0



def dfs(i, j, sum, count):
    global ans
    if count == 4:
        if ans < sum:
            ans = sum
        return
    else:
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == False:
                    visited[nx][ny] = True
                    dfs(nx, ny, sum + arr[nx][ny], count + 1)
                    visited[nx][ny] = False

                    
def middle(x,y):
    global ans
    sum = arr[x][y]

    ## x, y가 모서리면 ㅗ 모양은 아예 불가능
    if x == 0:
        if y == 0 or y == m-1:
            return
    elif x == n-1:
        if y == 0 or y == m-1:
            return

    case = []
    # ㅜ
    if 0<= x+1 < n and 1<= y < m-1:
        case.append(sum + arr[x+1][y] + arr[x][y-1] + arr[x][y+1])
    
    # ㅗ
    if 1 <= x < n and 1 <= y < m-1:
        case.append(sum + arr[x-1][y] + arr[x][y-1] + arr[x][y+1])
    
    # ㅏ
    if 1 <= x < n-1 and 0 <= y < m - 1:
        case.append(sum + arr[x-1][y] + arr[x+1][y] + arr[x][y+1])
    # ㅓ
    if 1 <= x < n-1 and 1 <= y < m:
        case.append(sum + arr[x-1][y] + arr[x+1][y] + arr[x][y-1])
    
    ans = max(ans, max(case))


for i in range(n):
    for j in range(m):
        middle(i, j)
        visited[i][j] = True
        dfs(i, j, arr[i][j], 1)
        visited[i][j] = False

        
print(ans)
