import sys 
input = sys.stdin.readline

n, k = map(int, input().split())

for _ in range(n):
    word = input()
    word = word[4:-4]

