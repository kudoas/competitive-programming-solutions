a, b, c, d = map(int, input().split())

start = max(a, c)
stop = min(b, d)
ans = stop-start

print(0 if ans < 0 else ans)
