# 이분 탐색
import math
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

titles = []
scores = []
for i in range(n):
    title, score = input().split()
    titles.append(title)
    scores.append(int(score))

answers = []

def find(target):
    s = 0
    e = len(scores) - 1
    while s <= e:
        mid = (s + e) // 2
        if scores[mid] > target:
            e = mid - 1
        else:
            s = mid + 1
    return s

q = []
for i in range(m):
    q.append(int(input()))

for qq in q:
    print(titles[find(qq)])
