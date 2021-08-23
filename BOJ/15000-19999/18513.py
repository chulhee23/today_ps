import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

w = list(map(int, input().split()))
visited = {}
q = deque()

for i in w:
    visited[i] = True
    q.append((i-1, -1))
    q.append((i+1, 1))

ans = 0
count = 0

while q:
    cur, dis = q.popleft()
    if cur not in visited:
        visited[cur] = True
        count += 1
        distance = abs(dis)
        ans += distance
        
        if count == k:
            break
    
    for dx in [-1, 1]:
        nx = cur + dx
        if nx not in visited:
            q.append((nx, dis + dx))
        
print(ans)