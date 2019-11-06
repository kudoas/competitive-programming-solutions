s = int(input())
se = set()

m = 1
while True:
    if s in se:
        ans = m
        break
    se.add(s)
    m += 1
    s = 3*s+1 if s & 1 else s//2

print(ans)
