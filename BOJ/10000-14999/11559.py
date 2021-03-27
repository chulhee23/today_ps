from collections import deque

row = 12
col = 6

arr = []
for _ in range(row):
    arr.append(list(input()))


visited = [[False] * col for _ in range(row)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()


answer = 0

moved = True

def bfs():
    moved = False
    for i in range(row):
        for j in range(col):
            if visited[i][j] or arr[i][j] == ".":
                visited[i][j] = True
                continue  
            
            queue.append((i, j))
            visited[i][j] = True
            count = 1
            move = []
            
            while queue:
                x, y = queue.popleft()
                move.append([x,y])
                
                if arr[x][y] == ".":
                    continue

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or nx >= row or ny < 0 or ny >= col:
                        continue
                    

                    if arr[nx][ny] == arr[x][y] and visited[nx][ny] == False:
                        
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                        count += 1
            
            if count >= 4:
                moved = True
                for xy in move:
                    arr[xy[0]][xy[1]] = "."
    
    return moved

def down():
    for j in range(col-1, -1, -1):
        tmp = []
        for i in range(row):
            tmp.append(arr[i][j])

        tmp = list(filter(lambda x: x != ".", tmp))
        while len(tmp) != row:
            tmp.insert(0, '.')
        for i in range(row):
            arr[i][j] = tmp[i]

while moved:
    visited = [[False] * col for _ in range(row)]
    moved = bfs()
    if moved: 
        answer += 1
    down()


print(answer)
