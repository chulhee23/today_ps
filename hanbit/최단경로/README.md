# 최단 경로 문제
- 한 지점 to 한 지점
- 한 지점에서 다른 모든 지점까지
- 모든 지점에서 다른 모든 지점

지점은 노드로, 도로는 그래프에서 간선으로 표현된다.

## 다익스트라 알고리즘
- 특정 노드에서 출발하여 다른 모든 노드로 가는 최단 경로 계산
- 음의 간선이 없을 때 정상 동작
- 그리디 알고리즘으로 분류
    - 매 상황에서 가장 비용이 적은 노드를 선택

    - DP 로도 분류되기도 한다. (길찾기는 보통 DP가 적용된다고 볼 수 있다.)


### 동작 과정
1. 출발 노드 설정
2. 최단 거리 테이블 초기화
3. 방문하지 않은 노드 중 최단거리가 가장짧은 노드 선택
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신
5. 3, 4 반복

최단 거리 테이블은 각 노드에 대한 현재까지의 최단 거리 정보를 가지고 있음.
더 짧은 경로를 찾으면 해당 경로로 갱신한다.


### 구현 방법
```python
INF = int(1e9) # 무한 의미하는 10억

graph[a].append((b,c)) # 방향이 있기 때문에, a번 노드에서 b번 노드로 가는 비용이 c

```


O(V)번에 걸쳐 최단 거리  노드를 매번 선형 탐색 -> 전체 시간 복잡도 O(V^2)
-> 좋지않다!

### 우선순위 큐
- 우선순위가 가장 높은 데이터를 먼저 삭제하는 자료구조
힙을 사용하여 구현 가능

- 최소 힙
- 최대 힙


```python

import heapq #최소 힙 제공
def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
        # heapq.heappush(h, -value) # 음수로 우선순위를 주어 최대힙처럼 사용 가능
        for i in range(len(h)):
            result.append(heapq.heappop(h))
        return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
# 힙에 넣었다가 꺼내는 과정 통해 정렬된다.
print(result)
# 결과 : 0,1,2,3,4,5,6,7,8,9

```

## 다익스트라 개선 구현 방법 (힙)
힙 자료구조를 사용하여 다익스트라 알고리즘 개선 가능하다.

- 현재 최단거리 노드 선택하는 최소 힙 사용


```python
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n+1)]

distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int(input().split()))
    graph[a].append((b,c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 최단 거리 노드 정보 꺼내기
        dist, now = heapq.heappop(q)

        # 현재 노드가 이미 처리된 적 있으면 무시
        if distnace[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if  cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("infinity")
    else:
        print(distance[i])
```
