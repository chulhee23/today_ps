import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

# n 세로
# m 가로
arr = []
red = [0, 0]
blue = [0, 0]


def init():
    for i in range(n):
        s = input().split()
        for ss in s[0]:
            if "R" in ss:
                red[0] = i
                red[1] = s[0].index("R")
            if "B" in ss:
                blue[0] = i
                blue[1] = s[0].index("B")

        arr.append([ss for ss in s[0]])


init()
visited = [[[[False] * m for _ in range(n)]
            for _ in range(m)] for _ in range(n)]


visited[red[0]][red[1]][blue[0]][blue[1]] = True
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
queue.append((red, blue, 1))


def move(node, dx, dy):
    x = node[0]
    y = node[1]
    cnt = 0
    while arr[x+dx][y+dy] != "#" and arr[x][y] != "O":
        x += dx
        y += dy
    return x, y, cnt


def solution():
    while queue:
        cur_red, cur_blue, count = queue.popleft()

        # 10회 안에 안 끝남
        # 어차피 bfs 이므로 이후의 node 모두 10회 이상
        if count > 10:
            break
        # move
        for i in range(4):
            next_red_x, next_red_y, move_count_red = move(
                cur_red, dx[i], dy[i])
            next_blue_x, next_blue_y, move_count_blue = move(
                cur_blue, dx[i], dy[i])

            if arr[next_blue_x][next_blue_y] != "O":
                if arr[next_red_x][next_red_y] == "O":
                    print(count)
                    return

                if next_red_x == next_blue_x and next_red_y == next_blue_y:
                    if move_count_red > move_count_blue:
                        next_red_x -= dx[i]
                        next_red_y -= dy[i]
                    else:
                        next_blue_x -= dx[i]
                        next_blue_y -= dy[i]

                if not visited[next_red_x][next_red_y][next_blue_x][next_blue_y]:
                    queue.append(([next_red_x, next_red_y], [
                                 next_blue_x, next_blue_y], count + 1))
                    visited[next_red_x][next_red_y][next_blue_x][next_blue_y] = True

    print(-1)


solution()
