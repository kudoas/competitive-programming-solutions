a, b, c, x, y = map(int, input().split())

ans = 0

if a+b >= c*2:
    ans = min(x, y)
