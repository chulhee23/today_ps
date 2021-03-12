from collections import deque


def solution(m, n, puddles):
    graph = [ [1] * n for x in range(m)]
    for puddle in puddles:
        x = puddle[0] - 1
        y = puddle[1] - 1
        graph[x][y] = 0

    queue = deque()
    queue.append([0,0])

    dx = [0, 1]
    dy = [1, 0]
    # 아래, 오른
    answer = 0

    while queue:
        tmp = queue.popleft()
        x = tmp[0]
        y = tmp[1]

        for i in range(2):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 0:
                continue
            
            queue.append([nx, ny])
            if nx == m - 1 and ny == n - 1:
                answer += 1
                
    r = 1000000007
    answer %= r
    return answer

print(solution(4, 3, [[2,2]] ) )