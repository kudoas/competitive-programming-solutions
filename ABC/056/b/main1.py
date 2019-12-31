W, a, b = map(int, input().split())

d = abs(a-b)
ans = max(0, d-W)

print(ans)
