from collections import deque
import copy
import sys
input = sys.stdin.readline


n, m = map(int, input().split())

arr = []
virus = deque()
for _ in range(n):
    tmp = list(map(int, input().split()))
    if 2 in tmp:
        virus.append((_, tmp.index(2)))
    arr.append(tmp)
    



wall_arr = wall(0, 0, copy.deepcopy(arr), 0)


def wall(i, j, arr, count):
    if count == 3:
        return arr

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(i, j, arr, 1)
                
