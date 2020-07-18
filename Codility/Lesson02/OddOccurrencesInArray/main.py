from collections import Counter


def solution(A):
    c = Counter(A)
    for k, v in c.items():
        if v % 2 == 1:
            return k
