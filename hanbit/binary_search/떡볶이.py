
# 1
n, m = map(int, input().split())

array = list(map(int, input().split()))

answer = 0

array = sorted(array, reverse=True)

maximum = array[0]
array = [maximum - h for h in array]

while m <= sum(array):
    maximum -= 1
    array = list(map(lambda h: h-1 if h > 0 else h, array))
    print(array)
print(maximum)
print(array)

        
# 2
'''
현재 이 높이로 자르면 조건을 만족할 수 있는가?
만족 여부에 따라 탐색 범위를 좁힌다
큰 범위? -> 우선 이진 탐색을 떠올리자.
위의 풀이는 시간초과.
'''

start = 0 
end = max(array)
result = 0

while (start <= end):
    total = 0
    mid = (start + end)//2
    for x in array:
        if x > mid:
            total += x - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
