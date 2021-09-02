import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()
visited = {}

def dfs(result, visited, m):
    if len(result) == m:
        result = list(str(i) for i in result)
        tmp = " ".join(result)
        if tmp not in visited:
            print(tmp)
            visited[tmp] = True
        return
    
    for idx, num in enumerate(nums):
        l = result[-1]
        if l <= num:
            result.append(num)
            dfs(result, visited, m)
            result.pop()


for idx, num in enumerate(nums):
    result = [num]

    dfs(result, visited, m)
