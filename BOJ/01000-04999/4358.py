import sys
from collections import defaultdict
input = sys.stdin.readline


trees = defaultdict(int)
count = 0

while True:
    tree = input().rstrip()
    if not tree:
        break
    trees[tree] += 1
    count += 1

arr = list(trees.keys())
arr.sort()
for tree in arr:
    print("%s %.4f" %(tree, trees[tree] / count * 100))
