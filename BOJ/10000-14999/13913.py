from collections import deque

n, k = map(int, input().split())

queue = deque()
queue.append((n, 0))

visited = [-1] * 100001

while queue:
    cur, count = queue.popleft()
    if cur == k:
        print(count)
        break

    if cur + 1 < 100001 and visited[cur+1] == -1:
        queue.append((cur + 1, count + 1))
        visited[cur + 1] = cur
    if cur - 1 >= 0 and visited[cur-1] == -1:
        queue.append((cur - 1, count + 1))
        visited[cur - 1] = cur
    if cur * 2 < 100001 and visited[cur * 2] == -1:
        queue.append((cur * 2, count + 1))
        visited[cur * 2] = cur

path = []
for _ in range(count + 1):
    path.append(cur)
    bef = visited[cur]
    cur = bef

print(*path[::-1])
