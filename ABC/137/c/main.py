n = int(input())
S = sorted([sorted(input()) for _ in range(n)])

memo = {}
ans = 0

for i in range(n):
    si = ('').join(S[i])
    if si not in memo:
        memo[si] = 1
    else:
        memo[si] += 1
        ans += memo[si] - 1

print(ans)
