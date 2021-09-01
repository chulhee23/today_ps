import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = list( i for i in range(1, n + 1))

answers = []
def dfs(len, num, m, result):
    if len == m:
        print(result)
        result = [ str(i) for i in result ]
        
        answers.append("".join(result))
        return
    
    for nx in nums:
        if visited[nx] == False:
            visited[nx] = True
            result.append(nx)
            dfs(len + 1, nx, m, result)
            result.remove(nx)
            visited[nx] = False

for num in nums:
    visited = [False] * (n + 1)
    
    # 시작
    result = [num]
    visited[num] = True
    dfs(1, num, m, result)
    visited[num] = False

print("========")
print(answers)
