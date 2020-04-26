n, k = map(int, input().split())
MOD = 10**9 + 7

ans = 0
for a in range(k, n+2):
    smallest = a*(a-1)//2
    largest = smallest + a*(n-a+1)
    ans += largest - smallest + 1
    ans %= MOD

print(ans)
