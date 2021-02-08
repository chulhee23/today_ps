# 이진 탐색 알고리즘
- 순차탐색 : 리스트 안의 특정 데이터 찾이 위해 앞에서부터 하나씩 확인
- 이진 탐색 : **정렬된 리스트**에서 탐색범위를 절반씩 좁혀가며 데이터 탐색
    - 시작점과 끝점, 중간점을 이용해 탐색범위 설정


```python
# 재귀적 구현
def bs(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        # 중간 값보다 작으면 왼쪽으로
        return bs(arr, target, start, mid-1)
    else: 
        return bs(arr, target, mid+1, end)

# 반복문
def bs_loop(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return arr[mid] # 탐색 성공
        elif arr[mid] >  target:
            end = mid - 1
        else:
            start = mid + 1
    return None
    
``` 

하지만, 파이썬에선 이진 탐색 라이브러리가 존재합니다.

```python

from bisect import bisect_left, bisect_right

# ...

def count_by_range(a, l, r):
    right_index = bisect_right(a, r)
    left_index = bisect_left(a, l)
    return right_index - left_index

a = [1,2,3,3,3,3,4,4,8,9]
# 같은 것이 있는 배열에서 같은 수가 몇 개 존재하는지 확인 가능
print(count_by_range(a, 4, 4)
# expect 2
print(count_by_range(a, -1, 3)
# expect 6
```


## 파라메트릭 서치
최적화 문제를 결정 문제로 바꾸어 해결하는 기법.
- 특정 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
