import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

# n 세로
# m 가로
arr = [list(input().rstrip()) for _ in range(n)]


visited = [[[[False] * m for _ in range(n)]
            for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()


def pos_init():
    rx, ry, bx, by = 0, 0, 0, 0  # 초기화
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'R':
                rx, ry = i, j
            elif arr[i][j] == 'B':
                bx, by = i, j
    # 위치 정보와 depth(breadth 끝나면 +1)
    queue.append(([rx, ry], [bx, by], 1))
    visited[rx][ry][bx][by] = True


def move(node, dx, dy):
    x = node[0]
    y = node[1]
    cnt = 0
    while arr[x+dx][y+dy] != "#" and arr[x][y] != "O":
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt


def solution():
    pos_init()

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
                    print(
                        f"same position!!!: {next_red_x} {next_red_y}, move_count_red: {move_count_red}, move_count_blue: {move_count_blue}")
                    if move_count_red > move_count_blue:
                        next_red_x -= dx[i]
                        next_red_y -= dy[i]
                    else:
                        next_blue_x -= dx[i]
                        next_blue_y -= dy[i]

                print(
                    f"red: {next_red_x} {next_red_y},  blue: {next_blue_x} {next_blue_y}, count: {count}")
                if not visited[next_red_x][next_red_y][next_blue_x][next_blue_y]:
                    print("visit!")
                    visited[next_red_x][next_red_y][next_blue_x][next_blue_y] = True
                    queue.append(([next_red_x, next_red_y], [
                                 next_blue_x, next_blue_y], count + 1))

    print(-1)


solution()
