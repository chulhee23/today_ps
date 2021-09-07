import sys
input = sys.stdin.readline


n = int(input())
m = int(input())
edges = []
for i in range(m):
    a, b, w = (map(int, input().split()))
    edges.append([w, a, b])
edges.sort(key = lambda x: x[0])
parent = list(range(n + 1))

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = parent[x]
    y = parent[y]
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
    
sum = 0

for w, start, end in edges:
    if find(start) != find(end):
        union(start, end)
        sum += w
print(sum)

