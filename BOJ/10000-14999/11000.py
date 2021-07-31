import sys
import heapq


input = sys.stdin.readline

n = int(input())

q = [list(map(int, input().split())) for _ in range(n)]

q.sort(key = lambda x: x[0]) # 시작 시간으로 정렬

room = []
heapq.heappush(room, q[0][1])


for i in range(1, n):
    if q[i][0] < room[0]:
        heapq.heappush(room, q[i][1])
    else:
        # 이어서 회의
        heapq.heappop(room)
        heapq.heappush(room, q[i][1])

print(len(room))