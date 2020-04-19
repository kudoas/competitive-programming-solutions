n, a, b = map(int, input().split())
MOD = 10**9+7
ans = pow(2, n, MOD)-1
X = Y = 1
for i in range(1, b+1):
    Y = Y*i % MOD
    X = X*(n-i+1) % MOD
    if i == a or i == b:
        ans -= X*pow(Y, MOD-2, MOD)

print(ans % MOD)
