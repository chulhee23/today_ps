from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0

    