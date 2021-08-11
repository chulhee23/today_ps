import sys
input = sys.stdin.readline
print = sys.stdout.write
n, m = map(int, input().split())
arr = []

for i in range(n):
    name, ext = input().split('.')
    arr.append([name, 0, ext])

# dictionary 를 사용해서 탐색을 빠르게...!
dic = {}
for i in range(m):
    e = input()
    dic[e] = True

for i in range(n):
    if arr[i][2] not in dic:
        arr[i][1] = 1

arr.sort()

for item in arr:
    print(f'{item[0]}.{item[2]}')
