W, H, N = map(int, input().split())
minx, maxx = 0, W
miny, maxy = 0, H

for _ in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
        minx = max(x, minx)
    elif a == 2:
        maxx = min(x, maxx)
    elif a == 3:
        miny = max(y, miny)
    elif a == 4:
        maxy = min(y, maxy)

width = max(0, maxx-minx)
height = max(0, maxy-miny)

print(width*height)
