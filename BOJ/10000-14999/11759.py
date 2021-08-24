# 투 포인터
# 구간의 합
# 그냥 합하면 시간 초과 발생한다!
# 그 이유는 뭘까??
# 투포인터가 왜 빠르지??

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))
ans = []

sum_arr = [0] * (n + 1)
for i in range(1, n+1):
    sum_arr[i] = sum_arr[i-1] + arr[i-1]


for i in range(m):
    s, e = map(int, input().split())
    ans.append(sum_arr[e] - sum_arr[s-1])

for item in ans:
    print(item)