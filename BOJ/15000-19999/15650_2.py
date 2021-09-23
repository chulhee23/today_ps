import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(range(1, n + 1))

answer = []
def dfs(visited, result, m):
    if len(result) == m:
        result = [str(i) for i in result]
        answer.append(" ".join(result))
        return
    for num in nums:
        if visited[num] == False and result[-1] < num:
            result.append(num)
            visited[num] = True
            dfs(visited, result, m)
            result.pop()
            visited[num] = False


for num in nums:
    visited = [False] * (n + 1)
    visited[num] = True
    result = [num]
    dfs(visited, result, m)
    visited[num] = False

for a in answer:
    print(a)