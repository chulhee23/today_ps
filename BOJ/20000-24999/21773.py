import sys
import heapq

input = sys.stdin.readline

t, n = map(int, input().split())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    # id, time, priority

    # heapq.heappush(arr, [-tmp[2], tmp[0], tmp[1]])
    arr.append([-tmp[2], tmp[0], tmp[1]])
    # 우선순위, id, time
heapq.heapify(arr)


for i in range(t):
    item = heapq.heappop(arr)
    
    item[2] -= 1
    item[0] += 1
    sys.stdout.write(f'{item[1]}\n')
    if item[2] != 0:
        heapq.heappush(arr, item)
    
