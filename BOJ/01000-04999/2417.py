# 이분탐색
import sys

input = sys.stdin.readline

n = int(input())

left = 0
right = n
while left <= right:
    mid = (left + right) // 2
    if mid ** 2 < n:
        left = mid + 1
    else:
        right = mid - 1
        

print(left)
