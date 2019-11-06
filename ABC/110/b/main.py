n, m, x, y = map(int, input().split())
ls_x = list(map(int, input().split()))
ls_y = list(map(int, input().split()))

x = max(max(ls_x), x)
y = min(min(ls_y), y)

print('No War' if x < y else 'War')
