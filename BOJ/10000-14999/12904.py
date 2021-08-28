import sys
input = sys.stdin.readline

s = list(input().rstrip())
t = list(input().rstrip())

result = False
while t:
    if t[-1] == "A":
        t.pop()
    elif t[-1] == "B":
        t.pop()
        t.reverse()
    if s == t:
        result = True
        break

print(1 if result else 0)