import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

visited = [-1] * 100001 # 적절한 초기화 필요

queue = deque()
queue.append((n, 0))

ans = 0
while queue:
    cur, cnt = queue.popleft()
    # 목표 도달
    if cur == k:
        if visited[cur] == -1:
            visited[cur] = cnt
            ans += 1

        elif visited[cur] == cnt:
            ans += 1

    for nx in [cur+2, cur + 1, cur - 1]:
        if 0 <= nx < 100001:
            if visited[nx] == -1 or visited[nx] >= cnt + 1:
                if cnt + 1 > visited[nx] and visited[k] != -1:
                    continue
                queue.append((nx, cnt + 1))

print(visited[k])
print(ans)
