# 벽 또는 자기자신의 몸과 부딪히면 게임이 끝
import sys
input = sys.stdin.readline


def change_direction(move, count, direction):
    if count in move.keys():
        if direction == 0:
            if move[count] == 'L':
                direction = 2
            else:
                direction = 3
        elif direction == 1:
            if move[count] == 'L':
                direction = 3
            else:
                direction = 2
        elif direction == 2:
            if move[count] == 'L':
                direction = 1
            else:
                direction = 0
        elif direction == 3:
            if move[count] == 'L':
                direction = 0
            else:
                direction = 1
    return direction





n = int(input())
arr = [[0] * n for _ in range(n)]

k = int(input())
apples = []
for _ in range(k):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1

l = int(input())

move = {}

for _ in range(l):
    x, c = input().split()
    x = int(x)
    move[x] = c


# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


snake = [(0, 0)]

direction = 3

count = 1
while True:
    hx, hy = snake[0]
    
    nx = hx + dx[direction]
    ny = hy + dy[direction]
    
    if (nx, ny) in snake[1:] or (nx < 0 or ny < 0 or nx >= n or ny >= n):
        break

    tx, ty = snake[-1]

    # move
    if len(snake) > 1:
        for idx in range(len(snake)-1, 0, -1):
            snake[idx] = snake[idx - 1]

    # apple
    if arr[nx][ny] == 1:
        arr[nx][ny] = 0
        snake.append((tx, ty))
    snake[0] = (nx, ny)

    direction = change_direction(move, count, direction)


    count += 1

print(count)

