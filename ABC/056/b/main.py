w, a, b = map(int, input().split())

if a <= b:
    ans = b-(a+w)
else:
    ans = a-(b+w)

print(max(0, ans))
