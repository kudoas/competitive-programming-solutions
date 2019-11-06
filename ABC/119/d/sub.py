import bisect

A, B, Q = map(int, input().split())

S = [int(input()) for i in range(A)]
S.insert(0, -float("inf"))
S.append(float("inf"))

T = [int(input()) for i in range(B)]
T.insert(0, -float("inf"))
T.append(float("inf"))

X = [int(input()) for i in range(Q)]

for x in X:
    ans = float("inf")
    idx_a = bisect.bisect_right(S, x)
    idx_b = bisect.bisect_right(T, x)

    for s in [S[idx_a-1], S[idx_a]]:
        for t in [T[idx_b-1], T[idx_b]]:
            temp = abs(s-t) + min(abs(x-s), abs(x-t))
            if temp < ans:
                ans = temp
    print(ans)
