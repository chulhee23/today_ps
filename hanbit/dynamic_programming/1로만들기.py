# https://www.acmicpc.net/problem/1463


# 연산 방법
# 3으로 나누거나
# 2로 나누거나
# 1을 빼서
# 최종 1을 만드는 방법



n = int(input())

dp = [0 for _ in range(n+1)]

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2]+1
    if i % 3 == 0 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1

print(dp[n])
