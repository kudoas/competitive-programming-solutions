from collections import Counter

n, m = map(int, input().split())
A = list(map(int, input().split()))
half = n//2
for k, v in Counter(A).items():
    if v > half:
        ans = k
        break
else:
    ans = '?'
print(ans)
