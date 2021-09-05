import sys
input = sys.stdin.readline

n = int(input())

arr = [[' ' for i in range(n)] for j in range(n)]

def solve(x, y, size):
    n = size // 3

    if size == 3:
        arr[x][y:y+3] = ['*'] * 3
        arr[x + 1][y:y+3] = ['*', ' ', '*']
        arr[x + 2][y:y+3] = ['*'] * 3
        return
    
    solve(x, y, n)
    solve(x, y + n, n)
    solve(x, y + 2 * n, n)

    solve(x + n, y, n)
    solve(x + n, y + 2 * n, n)
    
    solve(x + 2 * n, y, n)
    solve(x + 2 * n, y + n, n)
    solve(x + 2 * n, y + 2 * n, n)


solve(0, 0, n)

for i in arr:
    for j in i:
        print(j, end='')
    print()
