import copy
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# test case

# 1. init
n, w, h = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]

# 폭탄 떨어뜨릴 곳 찾기


