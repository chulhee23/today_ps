# 얼음 틀 모양 주어졌을 때 
# 생성되는 최대 아이스크림 수

# 2차원 배열
# 1은 막힘 -> 방문.
# 0은 열림 -> 아직 방문X. 
# 0 인접한 0들 묶음 갯수를 파악
def dfs(x, y):
    # 범위 벗어나면 종료
    if x <= -1 or x >= n or \
            y <= -1 or y >= m:
        return False

    # 방문 전
    if graph[x][y] == 0:
        # 방문 처리
        graph[x][y] = 1

        # 상하좌우 재귀 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True

    return False


n, m = map(int, input())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1


print(result)
