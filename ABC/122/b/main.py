S = input()

m = 0
cnt = 0

for s in S:
    if s in 'A':
        cnt += 1
    elif s in 'C':
        cnt += 1
    elif s in 'G':
        cnt += 1
    elif s in 'T':
        cnt += 1
    else:
        cnt = 0
    m = max(m, cnt)
print(m)
