o = input()
e = input()

ans = ''

for s, t in zip(o, e):
    ans += s+t

if len(o) > len(e):
    ans += o[-1]

print(ans)
