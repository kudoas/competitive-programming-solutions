h, w = map(int, input().split())

mas = h*w

if h == 1 or w == 1:
    print(1)
    exit()
if mas % 2 == 0:
    print(mas//2)
else:
    print(mas//2+1)
