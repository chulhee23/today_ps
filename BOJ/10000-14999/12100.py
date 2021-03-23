import pdb
from collections import deque
n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

queue = deque()
queue.append((arr, 0))

answer = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 숫자만 pop
# 다시 채우기


def left(graph):
    for i in len(graph):
        arr = graph[i]
        
        arr = list(filter(lambda x: x != 0, arr))
        for idx in range(1, len(arr)):
            if arr[idx - 1] == arr[idx]:
                arr[idx - 1] *= 2
                arr[idx] = 0
        
        arr = list(filter(lambda x: x != 0, arr))

        while (len(arr) < len(graph[i])):
            arr.append(0)
        graph[i] = arr
    return graph

def rotate(graph):
    tmp = graph[:]
    for i in range(len(graph)):
        for j in range(len(graph)):
            tmp[j][i] = graph[i][j]

    return tmp


def right(graph):
    y = len(graph[0])
    for i in range(y):
        arr = graph[i]
        arr = list(filter(lambda x: x != 0, arr))
        for idx in range(len(arr)-1, 0, -1):
            if arr[idx - 1] == arr[idx]:
                arr[idx] *= 2
                arr[idx - 1] = 0
        arr = list(filter(lambda x: x != 0, arr))

        while (len(arr) < y):
            arr.insert(0, 0)
        graph[i] = arr
    return graph

def bottom(graph):
    for j in range(len(graph[0])):
        arr = []
        for i in range(len(graph)):
            if graph[i][j] != 0:
                arr.append(graph[i][j])

        for idx in range(1, len(arr)):
            if arr[idx - 1] == arr[idx]:
                arr[idx] *= 2
                arr[idx - 1] = 0
        arr = list(filter(lambda x: x != 0, arr))

        while (len(arr) < len(graph)):
            arr.insert(0, 0)

        for i in range(len(graph)):
            graph[i][j] = arr[i]

    return graph

def top(graph):
    for j in range(len(graph[0])):
        arr = []
        for i in range(len(graph)):
            if graph[i][j] != 0:
                arr.append(graph[i][j])

        for idx in range(len(arr) - 1, 0, -1):
            if arr[idx - 1] == arr[idx]:
                arr[idx - 1] *= 2
                arr[idx] *= 0
        arr = list(filter(lambda x: x != 0, arr))
        while (len(arr) < len(graph)):
            arr.append(0)
        for i in range(len(graph)):
            graph[i][j] = arr[i]

    return graph



def dfs(graph):
    return graph



m = 0
for arr in answer:
    for a in arr:
        if m < max(a):
            m = max(a)
print(m)


# def bfs():
#     visited = []
#     while queue:
#         graph, count = queue.popleft()
#         visited.append(graph)

#         if count == 5:
#             answer.append(graph)
#         elif (count < 5):
#             count += 1

#             tmp = graph
#             l = left(tmp.copy())
#             r = right(tmp.copy())
#             t = top(tmp.copy())
#             b = bottom(tmp.copy())

#             if l not in visited:
#                 queue.append((l, count))

#             if r not in visited:
#                 queue.append((r, count))

#             if t not in visited:
#                 queue.append((t, count))

#             if b not in visited:
#                 queue.append((b, count))
