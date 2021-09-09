# 다익스트라
import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = 10e9

# x로부터 최단거리 k 인 도시를 모두 출력
n, m, k, x = map(int, input().split())
graph = [[] for i in range(n+1)]

heap = []
for i in range(m):
    start, end = map(int, input().split())
    graph[start].append((1, end))

distance =  [INF] * (n + 1)
distance[x] = 0

heappush(heap, [0, x])
while heap:
    dist, nxt = heappop(heap)
    for n_cost, n_node in graph[nxt]:
        cost = n_cost + dist
        if cost < distance[n_node]:
            distance[n_node] = cost
            heappush(heap, (cost, n_node))

result = False
for idx, dist in enumerate(distance):
    if dist == k:
        result =True
        print(idx)

if result == False:
    print(-1)

