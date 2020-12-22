a = 1000 - int(input())

coins = [500, 100, 50, 10, 5, 1]

answer = 0
for i, v in enumerate(coins):
    tmp = a // v
    if tmp != 0:
        a -= v*tmp
        answer += tmp
    else: 
        continue
    
    if a == 0:
        break

print(answer)
