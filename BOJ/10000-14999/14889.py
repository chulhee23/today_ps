import itertools
import sys

input = sys.stdin.readline


n = int(input())

arr = [ list(map(int , input().split())) for _ in range(n)]


members = [i for i in range(n)]
start_teams = itertools.combinations(members, n//2)
# link 구하기 위해서 set 자료형 사용!
members = set(members)

ans = sys.maxsize
for start_team in start_teams:
    start = set(list(start_team))
    start_team_pairs = list(itertools.combinations(start, 2))

    link = list(members - start)
    link_team_pairs = list(itertools.combinations(link, 2))
    
    start_sum = 0
    link_sum = 0
    
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if j > i:
                if (i, j) in start_team_pairs:
                    start_sum += arr[i][j] + arr[j][i]
                    
                if (i, j) in link_team_pairs:
                    link_sum += arr[i][j] + arr[j][i]
    
    ans = min(abs(start_sum - link_sum), ans)
    


print(ans)


