# 서로소 집합 자료구조
- 합집합 (union)
  - 두 원소가 포함된 집합을 하나의 집합으로 합치는 연산
- 찾기 (find)
  - 특정 원소가 속한 집합이 어떤 집합인지 알려준다

## 동작 과정
1. 합집합 연산을 확인하여, 서로 연결된 두 노드를 확인한다.
   1. A와 B의 루트노드를 각각 찾는다.
   2. 부모 노드 A'과 B' 으로 서로 다를 경우 같은 집합으로 합치기 위해 A'을 B'의 부모노드로 설정
2. 모든 합집합 연산을 처리할 때까지 반복

parent 배열의 원소가 같은 경우 하나의 집합임을 알 수 있다!
연결성을 통해 집합의 특징을 알 수 있다.

찾기 함수는 모든 노드를 반복하게 되면 O(V) 만큼 시간 복잡도 갖게 된다.
이를 해결하기 위해 부모 노드의 값을 그냥 루트 노드로 갱신해둔다!

```python
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, b)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = list(range(v + 1))

# union 연산 수행
for edge in range(e):
    start, end = map(int, input().split())
    union_parent(parent, start, end)

```


