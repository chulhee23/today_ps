import sys
input = sys.stdin.readline

N = int(input())
cities = list(map(int, input().split()))
budgets = int(input())  # 예산
start, end = 0, max(cities)  # 시작 점, 끝 점

# 이분 탐색
while start <= end:
    mid = (start + end) // 2
    total = 0  # 총 지출 양
    
    # O(n) 임에도, n 값 자체가 10000 이하이므로 비교적 안전!
    # O(n*log n) 정도!
    for i in cities:
        if i > mid:
            total += mid
        else:
            total += i
    
    if total <= budgets:  # 지출 양이 예산 보다 작으면
        start = mid + 1
    else:  # 지출 양이 예산 보다 크면
        end = mid - 1

print(end)