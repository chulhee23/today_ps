# 시뮬레이션, 삼성, 주사위 문제
# 주사위 면 고정. 값만 변경

import sys
input = sys.stdin.readline

# 세로 n 
n, m, x, y, k = map(int, input().split())
arr = []


for i in range(n):
    arr.append(list(map(int, input().split())))

moves = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0]

def roll(direction):
    if direction == 1:
        # 동
        dice[2], dice[0], dice[4],dice[5] = dice[0], dice[4], dice[5], dice[2]
    elif direction == 2:
        # 서
        dice[0], dice[2], dice[5], dice[4] = dice[2], dice[5], dice[4], dice[0]
        
    elif direction == 3:
        # 북
        dice[0], dice[3], dice[5], dice[1] = dice[1], dice[0], dice[3], dice[5]
    else:
        # 남
        dice[0], dice[1], dice[5], dice[3] = dice[3], dice[0], dice[1], dice[5]
        

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for move in moves:
    nx = x + dx[move - 1]
    ny = y + dy[move - 1]
    
    if 0<= nx < n and 0<= ny < m:
        roll(move)
        x = nx
        y = ny
        if arr[x][y] != 0:
            dice[5] = arr[x][y]
            arr[x][y] = 0
        else:
            arr[x][y] = dice[5]
        print(dice[0])




