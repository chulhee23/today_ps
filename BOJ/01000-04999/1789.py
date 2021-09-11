# 이분탐색

import sys
input = sys.stdin.readline

s = int(input())

ans = 0
left = 1
right = s

# 가장 많으려면, 1부터 쭉 더해온 값이어야 함 -> mid 값과 동일하겠지!
while left <= right:
    mid = (left + right) // 2
    if mid * (mid + 1) // 2 <= s:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)