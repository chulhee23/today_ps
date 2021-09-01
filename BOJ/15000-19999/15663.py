import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))

nums.sort()
answers = {}
def dfs(result, visited, m):
    if len(result) == m:
        result = list(str(i) for i in result)
        ans = " ".join(result)
        if ans not in answers:
            print(ans)
            answers[ans] = True

    for idx, num in enumerate(nums):
        if visited[idx] == False:
            visited[idx] = True
            result.append(num)
            dfs(result, visited, m)
            result.pop()
            visited[idx]= False
        
for idx, num in enumerate(nums):
    result = [num]
    visited = [False] * n
    visited[idx] = True

    dfs(result, visited, m)
    visited[idx] = False
    
