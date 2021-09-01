import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(i for i in range(1, n+1))
answers = []

def dfs(result, visited, m):
    if len(result) == m:
        result = list(str(i) for i in result)
        res = " ".join(result)
        answers.append(res)
        return

    for num in nums:
        if visited[num] == False and num > result[-1]:
            visited[num] = True
            result.append(num)
            dfs(result, visited, m)
            visited[num] = False
            result.pop()


for num in nums:
    result = [num]
    visited = [False] * (n+1)

    visited[num] = True
    dfs(result, visited, m)
    visited[num] = False

for ans in answers:
    print(ans)