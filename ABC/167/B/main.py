# a, b, c, k = map(int, input().split())
# ans = min(a, k)
# k -= a
# if k > 0:
#     k -= b
# if k > 0:
#     ans -= k

# print(ans)

a, b, c, k = map(int, input().split())
if k <= a + b:
    print(min(a, k))
else:
    print(a-(k-(a+b)))
