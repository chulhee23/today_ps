a = int(input())

arr = list(map(int, input().split()))
b, c = map(int, input().split())

ans = 0
ans += len(arr)
for i in range(len(arr)):
    if arr[i] < b:
        arr[i] = 0
    else:
        arr[i] = arr[i] - b
    
    if arr[i] > 0:
        tmp = int((arr[i] - 1) / c)
        if (tmp >= 0):
            ans += tmp + 1

print(ans)
