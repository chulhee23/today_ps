from collections import Counter

clothes = [["yellow_hat", 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
def solution(clothes):
    counter = Counter([cat for _, cat in clothes])
    print(counter)
    all_possible = 1
    for key in counter:
        all_possible *= (counter[key] + 1)

    return all_possible - 1


solution(clothes)