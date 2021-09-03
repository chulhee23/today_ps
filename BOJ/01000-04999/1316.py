import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(input().rstrip())

ans = 0
for word in arr:
    visited = {}
    visited[word[0]] = True
    result = True
    for idx in range(1, len(word)):
        tmp = word[idx-1]
        if tmp != word[idx]:
            if word[idx] not in visited:
                visited[word[idx]] = True
            else:
                result = False
                break
        
    if result:
        ans += 1

print(ans)
