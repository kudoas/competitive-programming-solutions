def solution(A):
    A.sort()
    for i, v in enumerate(A, 1):
        if i != v:
            return i
    else:
        return len(A)+1


# test: missing_last
A = [1, 2, 3]
print(solution(A))
