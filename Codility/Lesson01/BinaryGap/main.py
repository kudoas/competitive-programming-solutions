def solution(N):
    bit = str(bin(N))[2:]
    cnt = 0
    ans = 0
    for b in bit:
        if b == '1':
            ans = max(ans, cnt)
            cnt = 0
        else:
            cnt += 1
    return ans


# test
n = 32
print(solution(n))
print(bin(n))
