def solution(X, Y, D):
    diff = Y - X
    jmp = -(-diff // D)
    return jmp


# test
x, y, d = 1, 4, 2
print(solution(x, y, d))
