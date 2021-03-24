from collections import deque

a, b = map(int, input().split())

queue = deque()
queue.append((a, 1))

answer = -1
while queue:
    num, count = queue.popleft()
    if num == b:
        answer = count
        break

    if num * 2 <= b:
        queue.append((num * 2, count + 1))
    
    if int(str(num) + "1") <= b:
        queue.append((int(str(num) + "1"), count + 1))

print(answer)
