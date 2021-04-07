from collections import deque

n, k = map(int, input().split())

queue = deque()
queue.append(n)
visited = [0] * 100001
ans = -1
while queue:
    x = queue.popleft()
    if x == k:
        ans = visited[x]
        break

    for nx in [x - 1, x+1, 2*x]:
        if 0 <= nx < 100001 and visited[nx] == 0:
            if nx == 2*x and x != 0:
                visited[nx] = visited[x]
                queue.appendleft(nx)
            else:
                visited[nx] = visited[x] + 1
                queue.append(nx)


print(ans)