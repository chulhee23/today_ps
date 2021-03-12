def solution(clothes):
    d = dict()
    for c in clothes:
        if c[1] in d:
            d[c[1]].append(c[0])
        else:
            d[c[1]] = [c[0]]

    print(d)
    a = []
    for arr in d.values():
        a.append(len(arr) + 1)
    answer = 1
    for x in a:
        answer *= x
    return answer -1

clothes = [["yellow_hat", 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
print(solution(clothes))