def solution(citations):
    citations.sort(reverse=True)

    h = len(citations)

    while h > 0:
        if (citations[h-1] >= h) and h == len(citations):
            return h

        if (citations[h-1] >= h) and (citations[h] <= h):
            return h

        h = h - 1

    return h


print(solution([2, 0, 6, 1, 5]))
print(solution([0,0,0,0,0,0]))
