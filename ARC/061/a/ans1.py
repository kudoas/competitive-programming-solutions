s = input()
n = len(s) - 1

ans = 0
for i in range(2**n):
    formula = s[0]
    for j in range(n):
        if (i >> j & 1):
            formula += '+'
        formula += s[j+1]
    ans += eval(formula)

print(ans)
