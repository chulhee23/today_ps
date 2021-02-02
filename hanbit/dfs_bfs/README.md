# DFS/BFS

- 그래프 탐색 알고리즘 dfs, bfs
- 코테에서 자주 등장하는 유형


## 스택
- 선입선출 자료구조
- 입구와 출구 동일


## 큐
- 선입후출 자료구조
- 입구와 출구가 뚫려있는 터널 같은 형태


```python
# 큐를 사용할 때는 반드시 deque 라이브러리 사용

from collections import deque
queue = deque()
# 삽입
queue.append(5)
queue.append(2)
queue.append(3)
# queue: 5, 2, 3

# 삭제
queue.popleft()
# queue: 2, 3

# 역순으로
queue.reverse()
# queue: 3, 2
```


## 재귀함수(Recursive Function)
- 자기 자신을 다시 호출하는 함수
- DFS 에서 자주 사용

```python
def recursive_function():
    print('call recursive')
    recursive_function()
# 오류 발생. 파이썬에서 max recursion depth 가 정해져 있음(깊이 제한)
```
- 문제 풀이에서 반드시 종료 조건을 명시할 것.
```python
def recursive_function(i):
    if i > 100:
        return 
    print(i, 'call recursive')
    recursive_function(i+1)
```

- 재귀함수를 사용한 팩토리얼 함수 구현 예시
```python
def factorial_recursive(n):
    if n <= 1:
      return 1
    return n * factorial_recursive(n - 1)
```




- 최대 공약수(유클리드 호제법) 재귀함수 예시
```python
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

print(gcd(192, 162))
```

- 재귀 함수는 반복문으로 구현 가능
- 반복문, 재귀 함수 중 어떤 것이 유리한지 확인
- 함수는 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓인다.


# DFS (Depth-First Search)

- 깊이 우선 탐색
- 스택 자료구조, 혹은 재귀함수를 사용

1. 탐색 시작 노드를 스택에 삽입 및 방문 처리
2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그노드를 스택에 넣고 방문처리.
방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
3. 2번의 과정을 수행할 수 없을 때까지 반복.

```python
def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 표현한 2차원 리스트
graph = [
  [], # 0번 인덱스 정보. 1번 노드부터 시작
  [2,3,8], 
  [1, 7],
  [1, 4, 5],
  [1, 7],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]
visited = [False] * 9

dfs(graph, 1, visited)
```


## BFS(Breadth-First Search)
- 너비 우선 탐색
- 가까운 노드부터 우선 탐색
- 큐 자료구조 사용

1. 탐색 시작 노드를 큐에 삽입, 방문 처리
2. 큐에서 노드를 꺼낸 뒤 해당 노드의 인접 노드 중 방문하지 않은 모든 노드를 큐에 삽입하고 방문 처리
3. 2번 수행할 수 없을 때까지 반복

- 간선의 비용이 동일할 때 최단 거리 구할 수 있다.

```python
from collections import deque
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
              
graph = [
  [], # 0번 인덱스 정보. 1번 노드부터 시작
  [2,3,8], 
  [1, 7],
  [1, 4, 5],
  [1, 7],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]
visited = [False] * 9

bfs(graph, 1, visited)
```