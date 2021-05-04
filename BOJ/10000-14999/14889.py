# 백트래킹
from itertools import combinations, permutations

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]


members = list(range(0, n))

start = combinations(members, n // 2)

ans = float('inf')

for team1 in start:
    team2 = list(set(members) - set(team1))
    team1 = list(team1)

    tmps = permutations(team1, 2)
    sum1 = 0
    for tmp in tmps:
        i = tmp[0]
        j = tmp[1]
        sum1 += arr[i][j]
    
    tmps = permutations(team2, 2)
    sum2 = 0
    for tmp in tmps:
        i = tmp[0]
        j = tmp[1]
        sum2 += arr[i][j]
    ans = min(abs(sum1 - sum2), ans)
print(ans)