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
    y = len(graph[0])
    for i in range(y):
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


def solution():
    while queue:
        graph, count = queue.popleft()
        if count == 5:
            answer.append(graph)
        elif (count < 5):
            count += 1

            for i in range(4):
                tmp = graph
                l = left(tmp)
                r = right(tmp)
                t = top(tmp)
                b = bottom(tmp)

                queue.append((l, count))
                queue.append((r, count))
                queue.append((t, count))
                queue.append((b, count))


solution()
m = 0
print(len(answer))
for arr in answer:
    for a in arr:
        if m < max(a):
            m = max(a)
print(m)


# def left(graph):
#     for i in range(n):
#         moved = []
#         for j in range(n-1):
#             if graph[i][j] == graph[i][j+1]:
#                 graph[i][j] = graph[i][j] + graph[i][j+1]
#                 graph[i][j+1] = 0
#                 moved.append(j+1)
#         if moved:
#             for j in range(n-1):
#                 if j in moved:
#                     graph[i][j] = graph[i][j+1]
#                     graph[i][j+1] = 0
#     return graph

# def right(graph):
#     for i in range(n):
#         moved = []
#         for j in range(1, n):
#             if graph[i][j-1] == graph[i][j]:
#                 graph[i][j] = graph[i][j] + graph[i][j-1]
#                 graph[i][j-1] = 0
#                 moved.append(j-1) # 0이 되는 부분
#         if moved:
#             for j in range(1, n+1):
#                 if j in moved:
#                     graph[i][j-1] = graph[i][j] # 0 자리로 이동
#                     graph[i][j] = 0 # 원래 자리 0
#     return graph
