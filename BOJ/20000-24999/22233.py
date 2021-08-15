import sys

n, m = map(int, input().split())

arr = []
keywords = {}
for i in range(n):
    cur = input()
    if cur in keywords:
        continue
    keywords[cur] = 1

ans = n
for i in range(m):
    cur_keywords = list(input().split(','))
    for use in cur_keywords:
        if use in keywords and keywords[use] == 1:
            keywords[use] += 1
            ans -= 1

    arr.append(ans)

for item in arr:
    print(item)