# 다이나믹 프로그래밍
메모리를 적절히 사용하여 수행시간 효율성을 향상
- 탑 다운(하향식)
- 바텀 업(상향식)

## DP 조건
1. 최적 부분 구조
    - 큰문제를 작은 문제로 나눌 수 있으며, 작은 문제의 답을 모아 큰 문제 해결
2. 중복되는 부분 문제
    - 동일한 작은문제를 반복하여 해결

#### 예시 - 피보나치 수열

```python
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return  fibo(x-1) + fibo(x-2)
```
지수 시간 복잡도를 가지게 됩니다.
( fibo(2)가 여러 번 호출되기 때문! )
빅오 표기법 : O(2^N)
**중복이 발생 -> 중복을 해결해야 한다.** 


### 효율적인 해법
우선 다음 조건을 만족하는지 확인하자!
**1. 최적 부분 구조 : 큰 문제를 작은 문제로 나눌 수 있다.**
**2. 중복되는 부분 문제 : 동일한 작은 문제를 반복적으로 해결한다.**

#### 메모이제이션
한 번 계산한 결과를 메모리 공간에 메모하는 기법.
-> 캐싱
주로 탑다운 방식에서 사용한다.

```python
# 탑다운
d = [0] * 100
def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]
```

```python
# 바텀 업
d = [0] * 100

d[1] = 1
d[2] = 1
n=99
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]
```

메모이제이션을 사용하면 시간복잡도는 O(N)으로 줄어들게 된다.



# 다이나믹 프로그래밍 vs 분할정복
- 둘다 모두 최적 부분 구조를 가질 때 사용 가능
    - 큰문제를 작은 문제로 나눌 수 있고, 작은 문제의 답을 모아서 큰 문제를 해결할 수 있는 상황
- 차이점은 부분 문제의 중복
    - DP는 각 부분 문제들이 서로 영향을 미치며 부분 문제가 중복
    - 분할 정복 문제에서는 동일한 부분 문제가 반복적으로 계산되지 않음



## 분할정복의 대표 : 퀵 정렬
- 한 번 기준 원소(Pivot)가 자리를 변경하여 자리를 잡으면 그 기준 원소의 위치는 바뀌지 않음
- 분할 이후 해당 피벗을 다시 처리하는 부분 문제는 호출하지 않음


## DP 문제 접근 방법
- 문제가 DP 유형인지 파악
- 먼저 그리디, 구현, 완전 탐색 등의 아이디어로 문제를 해결할 수 있는지 검토할 수 있다.
    - 다른 알고리즘으로 풀이 방법이 떠오르지 않으면 DP를 고려하자.
    - 재귀 함수로 비효율적인 완전 탐색 프로그램을 작성한 뒤에 (탑다운) 
    작은 문제에서 구한 답이 큰 문제에서 그대로 사용될 수 있으면
    코드를 개선하는 방법을 사용할 수 있다.
    - 일반 코테 수준에서는 기본 유형의 DP 문제가 출제되는 경우가 많다.

