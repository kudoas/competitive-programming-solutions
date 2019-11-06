a, b = map(int, input().split())
ans = a+b

print(round(ans/2) if ans % 2 == 0 else 'IMPOSSIBLE')
