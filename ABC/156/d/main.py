n, a, b = map(int, input().split())
mod = 10**9 + 7

ans = pow(2, n, mod)-1
product = 1
div = 1

# 全く分からん
for i in range(1, b+1):
    product = product * (n-i+1) % mod
    div = div*i % mod
    if i == a or i == b:
        ans -= product * pow(div, mod-2, mod)

print(ans % mod)
