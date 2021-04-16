import sys
input = sys.stdin.readline

n = int(input())
arr = [ list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]


dx = [1, 0]
dy = [0, 1]

dp[0][0] = 1
for i in range(n):
    for j in range(n):
        cur = arr[i][j]
        if cur > 0:
            if 0<= i + cur < n:
                dp[i+cur][j] += dp[i][j]
            
            if 0<= j + cur < n:
                dp[i][j+cur] += dp[i][j]

print(dp[-1][-1])





# BFS로 잘못된 풀이
'''
잘못된 근거
- 문제에 힌트가 있다.
전체 경로의 수 2^63-1개가 나올 수 있는데, 이를 하나씩 헤는 것은 무리가 있다.
당연하게 여겨야 한다.
또한 엣지 케이스에 대해 항상 주의하면서 짜자.
'''
# from collections import deque

# n = int(input())
# arr = [ list(map(int, input().split())) for _ in range(n)]

# queue = deque()
# queue.append((0, 0))

# dx = [1, 0]
# dy = [0, 1]

# ans = 0

# while queue:
#     x, y = queue.popleft()
#     weight = arr[x][y]
#     for i in range(2):
#         if arr[x][y] == 0:
#             continue

#         nx = x + dx[i] * weight
#         ny = y + dy[i] * weight

#         if nx == n-1 and ny == n - 1:
#             ans += 1
#             continue
        
#         if 0 <= nx < n and 0 <= ny < n:
#             if arr[nx][ny] != 0:
#                 queue.append((nx, ny))

# print(ans)
