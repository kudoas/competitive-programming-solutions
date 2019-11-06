import bisect

inf = float("inf")
ans = 0

a, b, q = map(int, input().split())
S = [-inf]+[int(input()) for _ in range(a)]+[inf]
T = [-inf]+[int(input()) for _ in range(b)]+[inf]
X = [int(input()) for _ in range(q)]

S.sort()
T.sort()


for x in X:
    ans = float('inf')
    i = bisect.bisect_right(S, x)
    j = bisect.bisect_right(T, x)
    d = inf
    for s in [S[i-1], S[i]]:
        for t in [T[j-1], T[j]]:
            d1 = abs(s-t) + min(abs(x-t), abs(x-s))
            if d1 < ans:
                ans = d1
    print(ans)
