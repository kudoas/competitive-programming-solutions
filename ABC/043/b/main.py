# stuck

S = list(input())
stuck = []

for s in S:
    if s != 'B':
        stuck.append(s)
    elif s == 'B' and stuck:
        stuck.pop()

print(''.join(stuck))
