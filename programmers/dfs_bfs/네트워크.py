
def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for node in range(n):
        # 노드 방문 전
        # 이전 반복문에서 방문한 적이 없었다면,
        # 이전 노드와 연결되어있지 않음. 서로 다른 네트워크
        if visited[node] == False:
            dfs(n, computers, node, visited)
            answer += 1

    return answer
    
def dfs(n, computers, node, visited):
    visited[node] = True
    for connect in range(n):
        # 연결 여부 확인(자기 자신이 아니고, 연결되어 있는 경우)
        if connect != node and computers[node][connect] == 1:
            # 방문한 적이 없는 노드라면
            if visited[connect] == False:
                dfs(n, computers, connect, visited)


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print("------")
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
