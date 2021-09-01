import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(i for i in range(1, n+1))
answers = []

def dfs(result, m):
    if len(result) == m:
        result = list(str(i) for i in result)
        answers.append(" ".join(result))

        return

    for num in nums:
        result.append(num)
        dfs(result, m)
        result.pop()

for num in nums:
    # 케이스의 초기 조건
    result = [num]
    dfs(result, m)

for ans in answers:
    print(ans)
    