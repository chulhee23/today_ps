import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = []
ans = []
for i in range(n):
    x = int(input())
    if x != 0:
        tmp = 1 if x >= 0 else -1
        
        heapq.heappush(arr, [abs(x), tmp])
    elif x == 0:        
        if len(arr) == 0:
            ans.append(0)
        else:
            v, a = heapq.heappop(arr)
            ans.append(v*a)

for item in ans:
    print(item)