import math
def solution(brown, yellow):
    x = (brown + 4 + math.sqrt( (brown + 4) ** 2 - 16 * (brown + yellow)) ) / 4
    y = (brown + yellow) // x
    return [int(max(x, y)), int(min(x, y))]

print(solution(10, 2))


def solution2(brown, yellow):
    count = brown + yellow
    for n in range(1, count + 1, -1):
        if count % n != 0: # 약수가 아닌 경우
            continue
        m = count // n
        if (n - 2) * (m - 2) == yellow: # 가운데 타일의 개수
            return sorted([n, m], reverse=True) 
