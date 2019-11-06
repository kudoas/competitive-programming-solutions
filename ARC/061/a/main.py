s = input()
n = len(s)-1
ans = 0

for i in range(2**n):
    S = s[0]
    for j in range(n):
        if ((i >> j) & 1):
            S += '+'
        S += s[j+1]
    ans += eval(S)

print(ans)
