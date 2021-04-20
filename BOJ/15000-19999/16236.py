# 삼성
# BFS
# 아기 상어
import sys
from collections import deque

n = int(input())
arr = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * n for _ in range(n)]
