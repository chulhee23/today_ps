# 다익스트라
import sys
input = sys.stdin.readline

v, e = map(int(input().split()))

arr = [[0] * (v+1) for _ in range(v+1)]

k = int(input())


for i in range(e):
    u, v, w = map(int, input().split())
    