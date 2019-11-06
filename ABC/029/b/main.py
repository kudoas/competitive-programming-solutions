S = [input() for _ in range(12)]
c = 0

for s in S:
    if 'r' in s:
        c += 1

print(c)
