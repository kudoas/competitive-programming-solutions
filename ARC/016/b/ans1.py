n = int(input())
X = [input() for _ in range(n)]

ans = 0
for i in range(9):
    col = ['.'] + [row[i] for row in X]
    col = ''.join(col)
    ans += col.count('x') + col.count('.o') + col.count('xo')

print(ans)
