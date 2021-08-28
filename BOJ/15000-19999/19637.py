# if 문 대신, 이분탐색!

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
titles = []
arr = []
for i in range(n):
    title, score = input().split()
    titles.append(title)
    arr.append(int(score))

scores = []
for i in range(m):
    scores.append(int(input()))

def calc(score):
    s = 0
    e = len(arr) - 1
    while s <= e:
        mid = (s + e) // 2
        if arr[mid] < score:
            s = mid + 1
        else:
            e = mid - 1
    return s

ans = []
for score in scores:
    ans.append(titles[calc(score)])
for a in ans:
    print(a)