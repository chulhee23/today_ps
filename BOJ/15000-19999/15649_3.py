import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(range(1, n + 1))

per = permutations(nums, m)

for pp in per:
    print(*list(pp))
