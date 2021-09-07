# 크루스칼
# 유니온 파인드

import sys
input = sys.stdin.readline

v, e = map(int, input().split())

edge = []
for i in range(e):
    a, b, w = map(int, input().split())
    edge.append(w, a, b)

# 유니온 파인드
# 가중치 기준으로 작은 값부터 정렬
edge.sort(key = lambda x: x[0])

parent = list(range(v + 1))


def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])  # 경로 압축
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if b < a:
        parent[a] = b
    else:
        parent[b] = a


sum = 0
for w, start, end in edge:
    if find(start) != find(end):
        union(start, end)
        sum += w
print(sum)


