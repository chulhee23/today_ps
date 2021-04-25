# 컨베이어 벨트 위의 로봇
# 시뮬레이션
# 단계별 해법 그대로 따라가자

from collections import deque
n, k = map(int, input().split())
arr = deque(list(map(int, input().split())))

ans = 1
robot = deque(list([0]*n))

while True:
    # 벨트 회전
    arr.rotate(1)
    robot.rotate(1)
    robot[-1] = 0

    # 2
    for i in range(-2, -n-1, -1):
        if robot[i] == 1 and robot[i+1] == 0 and arr[i+1-n] > 0:
            robot[i] = 0
            # 한 칸에 하나씩
            robot[i+1] = 1
            # 내구소 감소
            arr[i+1-n] -= 1
    # 마지막 내리기
    robot[-1] = 0
    
    # 3
    if arr[0] > 0:
        robot[0] = 1
        arr[0] -= 1
    
    # 4
    if arr.count(0) >= k:
        break
    ans += 1


print(ans)
