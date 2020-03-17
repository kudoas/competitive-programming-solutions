from collections import Counter

n, k = map(int, input().split())
A = list(map(int, input().split()))

ans = 0

d = Counter(A)

if n <= k:
    print(0)
else:
    ls = d.most_common(k)
    print(k, d)
    print(ls)
    ans = n
    for key, val in ls:
        ans -= val


print(ans)
