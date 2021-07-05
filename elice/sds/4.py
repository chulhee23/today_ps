# 1
# 5 4
# 01000
# 00110
# 10001
# 01001

test = int(input())

for t in range(test):
    m, n = map(int, input().split())
    arr = list([0] * m for _ in range(n))
    for i in range(n):
        row = input()
        for j in range(m):
            if int(row[j]) == 1:
                arr[i][j] = int(row[j])
    
    
