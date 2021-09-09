# 플로이드 와샬
import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)
for k in range(n):
    for i in range(n):
        for j in range(n):
            if arr[i][k] == 1 and arr[k][j] == 1:
                arr[i][j] = 1   

for i in range(n):
    print(*arr[i])

