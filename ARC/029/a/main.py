n = int(input())
ls = [int(input()) for _ in range(n)]
ans = float('inf')

for i in range(2**n):
    a = 0
    b = 0

    for j in range(n):
        if ((i >> j) & 1):
            a += ls[j]
        else:
            b += ls[j]
    ans = min(ans, max(a, b))

print(ans)
