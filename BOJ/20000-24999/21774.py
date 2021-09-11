# 이분탐색
# fail
import sys
input = sys.stdin.readline

n, q = map(int, input().split())
logs = []
missions = []
for i in range(n):
    tmp = input().rstrip().split('#')
    logs.append([tmp[0], int(tmp[1])])

for i in range(q):
    tmp = input().rstrip().split('#')

    missions.append([tmp[0], tmp[1], int(tmp[2])])


