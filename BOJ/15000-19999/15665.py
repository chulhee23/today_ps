import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

answer = []
visited = {}
def solve(result, m):
    if len(result) == m:
        tmp = " ".join(map(str, result))
        if tmp not in visited:
            visited[tmp] = True
            answer.append(tmp)
        return
    
    for num in nums:
        result.append(num)
        solve(result, m)
        result.pop()

for num in nums:
    solve([num], m)

for ans in answer:
    print(ans)