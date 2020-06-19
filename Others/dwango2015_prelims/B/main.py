from math import factorial


def nC2(n):
    return factorial(n) // (factorial(n-2)*factorial(2))


S = input()
S = S.replace('25', '?')+'1'
nico = []
cnt = 0
for s in S:
    if s == '?':
        cnt += 1
    if s != '?':
        nico.append(cnt)
        cnt = 0
ans = 0
for n in nico:
    if n == 0:
        continue
    if n == 1:
        ans += 1
        continue
    ans += nC2(n) + n
print(ans)
