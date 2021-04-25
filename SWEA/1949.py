# 등산로
# DFS
# 원상태로 돌리면서 돌아와야함

# 삼성 모의 테스트

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

test_case = int(input())


def dfs(x, y, path, isConst):
    # 현재 시점의 ans
    global ans
    if ans < path:
        ans = path
    
    # 등산로 탐색.
    # 4방향 확인
    # 갈 수 있으면 visit True, 나오면서 False
    for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
                
            if visited[nx][ny] == 1:
                continue

            # 이동가능한가?
            if arr[x][y] > arr[nx][ny]:
                visited[nx][ny] = 1
                dfs(nx, ny, path + 1, isConst)
                visited[nx][ny] = 0 
                # 나오면서 원상 복구

            elif arr[x][y] <= arr[nx][ny] and not isConst:
                # 최소로 깎아야함
                for j in range(1, k+1):
                    arr[nx][ny] -= j 
                    if arr[x][y] > arr[nx][ny]:
                        # 공사 완료
                        isConst = True
                        visited[nx][ny] = 1
                        dfs(nx, ny, path + 1, isConst)
                        visited[nx][ny] = 0
                    arr[nx][ny] += j



# input
answers = []
for tc in range(1, test_case+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 높은 봉우리
    maxH = 0
    for i in range(n):
        for j in range(n):
            if maxH < arr[i][j]:
                maxH = arr[i][j]
    
    ans = 0

    for i in range(n):
        for j in range(n):
            if arr[i][j] == maxH:
                visited = [[0]* n for _ in range(n)]
                visited[i][j] = 1
                dfs(i, j, 1, False)
    
    answers.append(f"#{tc} {ans}")
print(answers)