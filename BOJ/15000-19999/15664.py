import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr =list(map(int, input().split()))

arr.sort()

visited = [False] * n
result = []

def solve(depth, idx, n, m):
    if depth == m:
        print(" ".join(map(str, result)))
        return
    overlap = 0
    for i in range(idx, n):
        if not visited[i] and overlap != arr[i]:
            result.append(arr[i])
            visited[i] = True
            overlap = arr[i]

            solve(depth + 1, i + 1, n, m)
            result.pop()
            visited[i] = False

solve(0, 0, n, m)