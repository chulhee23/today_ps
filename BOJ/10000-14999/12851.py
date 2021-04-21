# # bfs
# # 숨바꼭질 2

# import sys
# from collections import deque

# input = sys.stdin.readline

# n, k = map(int, input().split())

# queue = deque()
# queue.append(n)

# visited = [0] * 100001
# visited[n] = 0

# ans_count = 0
# ans_way = 0
# while queue:
#     x = queue.popleft()
#     count = visited[x]
#     if x == k:
#         ans_count = count
#         ans_way += 1
#         continue

#     for nx in [x-1, x+1, 2*x]:
#         if 0 <= nx < 100001:
#             if visited[nx] == 0 or visited[nx] == visited[x] + 1:
#                 queue.append(nx)
#                 visited[nx] = count + 1
                

# print(ans_count)
# print(ans_way)














# ########

import sys
from collections import deque

n, k = map(int, input().split())

queue = deque()
queue.append((n, 0))

ans = -1
ways = 0
visited = [0] * 100001
while queue:
    cur, time = queue.popleft()
    if cur == k:
        if ans == -1:
            ans = time
            ways += 1
        elif ans == time:
            ways += 1

    for nx in [cur -1 , cur + 1, cur * 2]:
        if 0<= nx < 100001:
            if visited[nx] == 0 or visited[nx] == visited[cur] + 1:
                visited[nx] = time + 1
                queue.append((nx, time + 1))


print(ans)
print(ways)
