s = input()
n = len(s) - 1

ans = 0
for i in range(2**n):
    op = ['-'] * n + ['-']
    for j in range(n):
        if (i >> j & 1):
            op[j] = '+'
    formula = ''
    for j in range(n+1):
        if op[j] == '+':
            formula += s[j] + '+'
        else:
            formula += s[j]
    ans += eval(formula)

print(ans)
