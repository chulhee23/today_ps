# 삼성 오후 1번 문제
# 구현

n, m = map(int, input().split())


arr = [list(map(int, input().split())) for _ in range(n)]
moves = []
for i in range(m):
    tmp = list(map(int, input().split()))
    moves.append([tmp[0] - 1, tmp[1]])

clouds = [[n-2, 0], [n-2, 1], [n-1, 0], [n-1, 1]]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
for i in range(m):
    # step 1.
    # 이동
    move = moves[i]
    next_clouds = []
    for cloud in clouds:
        x = cloud[0]
        y = cloud[1]
        d = move[0]
        s = move[1]
        nx = (n + x + dx[d] * s) % n
        ny = (n + y + dy[d] * s) % n
        next_clouds.append([nx, ny])

    # step 2.
    visited = [[False]* n for _ in range(n)]
    for cloud in next_clouds:
        x = cloud[0]
        y = cloud[1]
        arr[x][y] += 1
        visited[x][y] = True
    
    # step 3
    clouds = []

    # step 4
    cx = [-1, -1, 1, 1]
    cy = [-1, 1, -1, 1]
    for cloud in next_clouds:
        x = cloud[0]
        y = cloud[1]
        count = 0
        for i in range(4):
            nx = x + cx[i]
            ny = y + cy[i]

            if 0 <= nx < n and 0<= ny < n and arr[nx][ny] >= 1:
                count += 1

        arr[x][y] += count
        
    # step 5

    for i in range(n):
        for j in range(n):
            if arr[i][j] >= 2 and visited[i][j] == False:
                arr[i][j] -= 2
                clouds.append([i, j])

ans = 0
for i in range(n):
    ans += sum(arr[i])


print(ans)
