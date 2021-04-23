
def dfs(idx, computers, visited):
    visited[idx] = True
    
    network = computers[idx]
    for i in range(len(network)):
        if network[i] == 1 and visited[i] == False and i != idx:
            dfs(i, computers, visited)

def solution(n, computers):
    answer = 0
    n = len(computers)

    visited = [False] * n
    
    for i in range(n):
        if visited[i] == False :
            dfs(i, computers, visited)
            answer += 1
        


    return answer



# print("------")
# print(bfs_sol(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
# print(bfs_sol(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
print("------")
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
