# 병사 배치하기

# 병사 배치할 때 전투력 높은 순으로 내림차순할 예정

# 특정 위치의 병사 열외하는 방법으로 정렬
# 남은 병사 수는 최대 

# 가장 긴 증가하는 부분 수열
# d[i] 는 array[i]를 마지막원소로 갖는 부분 수열의 최대 길이
# 모든 0 <= j < i 에 대해, d[i] = max(d[i], d[j]+1) if array[j] < array[i]

n = int(input())

array = list(map(int, input().split()))

# LIS 문제로 변경
array.reverse()
dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# max(dp) : 가장 긴 증가하는 부분 수열
# n - max(dp) : 열외된 병사 수 
print(n - max(dp))
