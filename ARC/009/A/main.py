n = int(input())
ans = 0
for _ in range(n):
    a, b = map(int, input().split())
    ans += b*a
else:
    ans *= 1.05
    ans = int(ans)
print(ans)
