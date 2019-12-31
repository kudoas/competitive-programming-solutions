n = int(input())
ans = float('inf')

for i in range(1, 10**6+1):
    q, m = divmod(n, i)
    if m == 0:
        ans = min(ans, q+i)

print(ans-2)
