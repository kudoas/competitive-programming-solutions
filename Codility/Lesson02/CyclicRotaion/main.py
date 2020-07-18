def solution(A, K):
    n = len(A)
    if K != 0:
        K %= n
    for _ in range(K):
        first = A.pop(-1)
        A.insert(0, first)
    return A
