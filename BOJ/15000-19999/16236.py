# 삼성
# BFS
# 아기 상
import sys
from collections import deque

n = int(input())
arr = []
shark_pos = [0,0]
visited = [[False] * n for _ in range(n)]
for i in range(n):
    # tmp 선언 없이 메모리 아끼기
    arr.append(list(map(int, input().split())))
    if 9 in arr[-1]:
        shark_pos[0] = i
        shark_pos[1] = arr[-1].index(9)
        visited[i][arr[-1].index(9)] = True
        arr[i][arr[-1].index(9)] = 0
