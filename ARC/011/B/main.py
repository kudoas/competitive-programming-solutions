n = int(input())
W = list(input().lower().split())
luwis = [['z', 'r'], ['b', 'c'], ['d', 'w'], ['t', 'j'], ['f', 'q'], [
    'l', 'v'], ['s', 'x'], ['p', 'm'], ['h', 'k'], ['n', 'g']]

ans = []
for w in W:
    c = ''
    for s in w:
        p = 0
        for a, b in luwis:
            if s == a or s == b:
                c += str(p)
            p += 1
    if c:
        ans.append(c)

print(*ans)
