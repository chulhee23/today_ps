import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

sum_arr = [0] * (n + 1)
sum_arr[0] = arr[0]

for i in range(1, n + 1):
    sum_arr[i] = sum_arr[i -1] + arr[i-1]

ans = 0
for i in range(0, n):
    for j in range(i + 1, n + 1):
        if sum_arr[j] - sum_arr[i] == m:
            ans += 1
print(ans)