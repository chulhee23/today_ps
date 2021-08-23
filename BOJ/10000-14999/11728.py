# 투포인터

# 시간 제한	메모리 제한	
# 1.5 초	256 MB

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
for i in range(2):
    arr += list(input().split())

print(" ".join(sorted(arr)))


a, b = map(int, sys.stdin.readline().split())
a_list = list(map(int, sys.stdin.readline().split()))
b_list = list(map(int, sys.stdin.readline().split()))
answer_list = a_list + b_list
answer = ' '.join(map(str, sorted(answer_list)))
print(answer)