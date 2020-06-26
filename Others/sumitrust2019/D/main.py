n = int(input())
s = input()
pins = ['0' * (3-len(str(i))) + str(i) for i in range(1000)]
ans = 0
for p in pins:
    a, b, c, = p
    if a not in s:
        continue
    p1 = s.index(a)
    if b not in s[p1+1:]:
        continue
    # ここが味噌！
    p2 = s[p1+1:].index(b) + len(s[:p1+1])
    if c not in s[p2+1:]:
        continue
    ans += 1
print(ans)
