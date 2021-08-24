import sys
input = sys.stdin.readline


n, x = map(int, input().split())

arr = list(map(int, input().split()))

sum_arr = [0] * (n + 1)
for i in range(1, n+1):
    sum_arr[i] = sum_arr[i-1] + arr[i-1]

count = 0
s, e = 0, x
cur_max = [0, 0]
for i in range(x, n + 1):
    cur = sum_arr[i] - sum_arr[i-x]
    if cur_max[0] < cur:
        cur_max[0] = cur
        cur_max[1] = 1
    elif cur_max[0] == cur:
        cur_max[1] += 1

if (cur_max[0] == 0):
    print("SAD")
else:
    print(cur_max[0])
    print(cur_max[1])