import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

def solve(x, y, n):
    if (n == 2):
        tmp = sorted([arr[x][y], arr[x + 1][y], arr[x][y+1], arr[x+1][y+1]])
        return tmp[-2]


    nx = n // 2
    ans = []
    ans.append(solve(x, y, nx))
    ans.append(solve(x + nx, y, nx))
    ans.append(solve(x, y + nx, nx))
    ans.append(solve(x + nx, y + nx, nx))
    ans.sort()
    
    return ans[-2]

print(solve(0, 0, n))

