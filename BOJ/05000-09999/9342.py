# 정규식
import sys
import re

input = sys.stdin.readline

t = int(input())

words = [' ', 'A', 'B', 'C', 'D', 'E', 'F']


ans = []
for i in range(t):
    s = input().rstrip()
    p = re.compile('^[A-F]{0,1}A*F*C*[A-F]{0,1}$')
    m = p.match(s)

    if m:
        print("Infected!")
    else:
        print("Good")

