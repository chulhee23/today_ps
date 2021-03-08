from collections import deque


def bfs_sol(n, computers):
    answer = 0

    visited = [False for _ in range(n)]
    queue = deque()
    for node in range(n):
        if visited[node] == False:  # node 가 방문한 적이 없으면
            queue.append(node)  # queue에 추가한 뒤, 확인 들어가자.
            while queue:
                cur_node = queue.pop()
                visited[cur_node] = True  # 방문 처리
                for tmp_node in range(n):
                    #  현재 노드와 상대 노드가 연결 처리된 경우
                    #  상대 노드를 확인해봐야함. -> queue에 추가해서 돌리자.
                    if cur_node != tmp_node and computers[cur_node][tmp_node] == 1:  
                        if visited[tmp_node] == False:
                            queue.append(tmp_node)

            answer += 1
        else:
            # 방문한 적이 있다?
            # 이전 노드에서 방문처리가 되었으므로 연결이 되어 있음
            continue

    return answer


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


# dfs 에서 하는 일을 바라보자
def dfs(n, computers, node, visited):
    visited[node] = True
    for connect in range(n):
        # 연결 여부 확인(자기 자신이 아니고, 연결되어 있는 경우)
        if connect != node and computers[node][connect] == 1:
            # 방문한 적이 없는 노드라면
            if visited[connect] == False:
                dfs(n, computers, connect, visited)


print("------")
print(bfs_sol(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(bfs_sol(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
print("------")
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
