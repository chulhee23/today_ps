# 이분탐색
import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
cards.sort()

m = int(input())
candi = list(map(int, input().split()))

def find(x):
    start = 0
    end = len(cards) - 1
    while start <= end:
        mid = (start + end + 1) // 2
        
        if cards[mid] == x:
            return 1
        
        if cards[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return 0


ans = []
for cand in candi:
    ans.append(find(cand))
print(*ans)