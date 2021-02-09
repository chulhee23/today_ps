# n종류 화폐.
# m 원 완성
# 2종류, 2원 3원으로 15원 완성

n, m = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

print(coins)

d = [10001] * (m+1)
# inf : 특정 구성이 가능하지 않다는 의미
d[0] = 0

for k in coins:
    d[k] = 1


for i in range(n):
    for j in range(coins[i], m+1):

        if d[j - coins[i]] != 10001:
            d[j] = min(d[j], d[j - coins[i]] + 1)

if d[m] == 10001:
    print(-1)
else:

    print(d[m])
