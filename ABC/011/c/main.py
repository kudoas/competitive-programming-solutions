# n = int(input())
# NG = [int(input()) for _ in range(3)]

# for _ in range(100):
#     if n in NG:
#         continue
#     if n >= 3 and n-3 not in NG:
#         n -= 3
#     elif n >= 2 and n-2 not in NG:
#         n -= 2
#     elif n >= 1 and n-1 not in NG:
#         n -= 1
# print('YES' if n == 0 else 'NO')


from itertools import product

n = int(input())
NG = set(int(input()) for _ in range(3))
se = set()
se.add(0)

for _ in range(100):
    se = set(x+y for x, y in product(se, [0, 1, 2, 3]) if x+y <= 300)
    se -= NG

ans = 'YES' if n in se else 'NO'
print(ans)
