a, b = input().split()
a1, a2, a3 = map(int, a)
b1, b2, b3 = map(int, b)
ans = int(a) - int(b) + max(
    100 * (9 - a1), 100 * (b1 - 1), 10 * (9 - a2),
    10 * b2, 9 - a3, b3
)
print(ans)
