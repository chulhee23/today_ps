from collections import deque


def diff(word, other):
    count = 0
    for i in range(len(word)):
        if word[i] != other[i]:
            count += 1
    return count


def solution(begin, target, words):

    visited = [False] * len(words)
    queue = deque()
    queue.append((begin, 0))
    ans = 0
    while queue:
        word, count = queue.popleft()

        if word == target:
            return count

        for i in range(len(words)):
            nx = words[i]
            if diff(word, nx) == 1 and visited[i] == False:
                visited[i] = True
                queue.append((nx, count + 1))

    return ans
