import sys
input = sys.stdin.readline

n, k = map(int, input().split())

l = 0
r = n - 1
answer = False

def find(left, right):
    if left > right:
        return False
    
    mid = (left + right) // 2
    res = (mid + 1)*(-mid + n + 1)
    if res == k:
        return True
    else:
        if res > k:
            return find(left, mid - 1)
        else:
            return find(mid + 1, right)


print("YES" if find(l, r) else "NO")
