from collections import Counter

n = int(input())
A = list(map(int, input().split()))
C = Counter(A)
ans = 1
MOD = 10**9+7
for k, v in C.items():
    if k == 0 and v != 1:
        print(0)
        exit()
    if k != 0 and v != 2:
        print(0)
        exit()
    ans *= v
print(ans % MOD)
