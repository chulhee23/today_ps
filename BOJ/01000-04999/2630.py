import sys
input = sys.stdin.readline

n = int(input())

arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))


ans = [0, 0]

def divide(x, y, size):
    cur = arr[x][y]

    for i in range(x, x + size):
        for j in range(y, y + size):
            if cur != arr[i][j]:
                # divide
                n = size // 2
                divide(x, y, n)
                divide(x + n, y, n)
                divide(x, y + n, n)
                divide(x + n, y + n, n)
                return
    
    if cur == 0:
        ans[0] += 1
    else:
        ans[1] += 1
    
    return 

divide(0, 0, n)
print(ans[0])
print(ans[1])