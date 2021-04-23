# 투포인터
n, m = map(int, input().split())
arr = list(map(int, input().split()))

sum_arr = [0] * (n+1)

for i in range(1, n + 1):
    sum_arr[i] = sum_arr[i-1] + arr[i-1]

answer = 0

for i in range(n):
    for j in range(i+1, n +1):
        if sum_arr[j] < m:
            continue
        elif sum_arr[j] - sum_arr[i] > m:
            break
        elif sum_arr[j] - sum_arr[i] == m:
            answer+= 1
            break

print(answer)


# 일반 풀이
# 시간 초과 발생한다!

# count = 0
# for i in range(n-1):
#     for j in range(i, n):
#         if m == sum(arr[i:j]):
#             count += 1
# print(count)
