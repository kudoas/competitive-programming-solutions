s = input()
t = input()

cnt = 0

for s, t in zip(s, t):
    if s == t:
        cnt += 1

print(cnt)
