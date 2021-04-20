# https: // swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId = AV5-BEE6AK0DFAVl
# 점심 식사시간
# 모의 역량 테스트

from collections import deque

test_case = int(input())

def solution():
    # settings
    n = int(input())
    arr = []
    people = []
    stairs = []

    for i in range(n):
        tmp = list(map(int, input().split()))
        arr.append(tmp)
        for j in range(len(tmp)):
            item = tmp[j]
            if j != 1 or j != 0:
                stairs.append([i, j])
            if item == 1:
                people.append([i, j])


    # 계단 찾기
    





    



for _ in range(test_case):
    solution()
