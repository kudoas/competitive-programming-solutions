a, b, x = map(int, input().split())


def price(n):
    return a*n+b*int(len(str(n)))


left = 1
right = 10**9+1
while (right-left) > 1:
    mid = (left + right)//2
    if x < price(mid):
        right = mid
    else:
        left = mid
    print(left, mid, right)
