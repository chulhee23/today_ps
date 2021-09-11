import sys
input = sys.stdin.readline

k = int(input())
arr = list(map(int, input().split()))

mid = len(arr) // 2
root = arr[mid]
ans = [[] for _ in range(k)]

def find(array, lv):
    start = 0
    end = len(array)
    mid = end // 2
    root = array[mid]
    ans[lv].append(root)

    if start < mid:
        find(array[start:mid], lv + 1)
        find(array[mid + 1:end], lv + 1)

find(arr, 0)

for a in ans:
    print(*a)