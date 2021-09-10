# 이분탐색
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()



left = 0
right = len(arr) - 1
ans = arr[left] + arr[right]

al, ar = left, right

while left < right:
    s = arr[left] + arr[right]
    if abs(s) < abs(ans):
        ans = s
        al, ar = left, right
        if s == 0:
            break
    
    if s < 0:
        left += 1
    else:
        right -= 1

print(arr[al], arr[ar])
