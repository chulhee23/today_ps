from collections import deque

n, k = map(int, input().split())

queue = deque()

queue.append((n, 0, [n]))

while queue:
    cur, count, visited = queue.popleft()
    if cur == k:
        print(count)
        print(*visited, sep=" ")
        break
    if cur + 1 < 100000:
        
        queue.append((cur + 1, count + 1, visited + [cur + 1]))
    if cur - 1 >= 0:
        queue.append((cur - 1, count + 1, visited + [cur - 1]))
    if cur * 2 < 100000:
        queue.append((cur * 2, count + 1, visited + [cur * 2]))


