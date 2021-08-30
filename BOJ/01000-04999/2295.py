# 복습
import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))
arr.sort()

two = []
for i in range(n):
    for j in range(i, n):
        two.append(arr[i] + arr[j])
two.sort()

ans = 0

for i in range(n):
    for j in range(i, n):
        target = arr[j] - arr[i]
        s = 0
        e = len(two)
        while s < e:
            mid = (s + e) // 2
            if two[mid] == target:
                ans = max(ans, target + arr[i])
                break
            elif two[mid] < target:
                s = mid + 1
            else:
                e = mid - 1
print(ans)            

'''
아이디어가 굉장히 중요한 문제
단순하게 이분탐색하고 끝! 이 아니라,
이번 문제처럼 
2개를 묶거나 어떤 처리를 한 뒤 
한 쪽의 시간복잡도를 이분탐색으로 낮춘다!

'''