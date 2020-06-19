n = int(input())
TA = [tuple(map(int, input().split())) for _ in range(n)]
s, a = 1, 1
for d, f in TA:
    k = max(-(-a//d), -(-s//f))
    s, a = f*k, d*k
print(s+a)
