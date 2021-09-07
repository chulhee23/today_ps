# fail
# 분할정복..?
# 좀 애매한 분할정복
import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

count = 0
dx = [0, 0, 1, 1]
dy = [0, 1, 0, 1]
def solve(x, y, size):
    global count
    if size == 2:
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx == r and ny == c:
                print(count)
                return
            count += 1
    
    else:
        size //= 2
        solve(x, y, size)
        solve(x, y + size, size)
        solve(x + size, y, size)
        solve(x + size, y + size, size)

solve(0, 0, n ** 2)


# 2^10 * 2^10 배열은 메모리 초과!
# import sys
# input = sys.stdin.readline

# n, r, c = map(int, input().split())
# m = 2 ** n
# arr = [[0] * m for _ in range(m)]
# result = False
# def solve(x, y, row, first):
#     global r, c, result
#     if result:
#         return
    
#     if row == 2:
#         arr[x][y] = first
#         arr[x][y+1] = first + 1
#         arr[x+1][y] = first + 2
#         arr[x+1][y+1] = first + 3
#         return


#     nc = (row ** 2) // 4
#     n_row = row // 2
#     solve(x, y, n_row, first + nc * 0)
#     solve(x, y + n_row, n_row, first + nc * 1)
#     solve(x + n_row, y, n_row, first + nc * 2)
#     solve(x + n_row, y + n_row, n_row, first + nc * 3)

# solve(0, 0, m, 0)
# print(arr[r][c])
