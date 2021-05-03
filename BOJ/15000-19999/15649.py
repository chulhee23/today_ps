# 백트래킹
# n과 m
from itertools import permutations
n, m = map(int, input().split())

# arr = permutations(list(range(1, n+1)), m)

# for a in arr:
#     tmp = [str(aa) for aa in a]
#     print(" ".join(tmp))
    

nums = list(range(1, n+1))

def dfs(count, num, m):
    if count == m:
        print(result)
        return
    
    
    for next_num in (nums):
        if visited[next_num - 1] == False:
            visited[next_num - 1] = True
            result.append(next_num)
            dfs(count + 1, next_num, m)
            result.remove(next_num)
            visited[next_num - 1] = False

        


for num in (nums):
    visited = [False] * n
    result = [num]
    visited[num - 1] = True
    dfs(1, num, m)

