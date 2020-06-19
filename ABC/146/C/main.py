def price(n):
    global a
    global b
    return a * n + b * int(len(str(n)))


a, b, x = map(int, input().split())
left = 0
right = 10**9 + 1
while (right-left > 1):
    mid = (left + right) // 2
    print(left, mid, right)
    if price(mid) > x:
        right = mid
    else:
        left = mid
print(min(left, 10**9))

# if a+b > x:
#     print(0)
#     exit()
# candidate = x // a
# while True:
#     price = a*candidate + b*int(len(str(candidate)))
#     if price <= x:
#         break
#     candidate -= 1
# print(min(candidate, 10**9))
