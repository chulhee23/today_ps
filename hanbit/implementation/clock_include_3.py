# n시 59분 59초까지 3이 포함된 모든 경우의 수를 구하라.


# n = int(input())
n = 5
 # to sec
count = 0

max_t = n * (60 * 60) + 59 * 60 + 59

# bad
while n <= max_t:
    h = n // 3600
    m = (n - h * 3600) // 60
    s = n - 3600 * h - 60 * m

    if "3" in (str(h) + str(m) + str(s)):
        count += 1

    n += 1

print(count)


# good
h = 5
count = 0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if "3" in str(i) + str(j) + str(k):
                count += 1

print(count)