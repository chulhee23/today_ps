# 분할정복
import sys
input = sys.stdin.readline

k = int(input())

def recur(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n % 2:
        return 1 - recur(n // 2)
    else:
        return recur(n // 2)

print(recur(k - 1))