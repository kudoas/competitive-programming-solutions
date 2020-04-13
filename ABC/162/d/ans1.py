# pypy
n = int(input())
s = input()

ans = s.count('R') * s.count('G') * s.count('B')
rgb = {'R', 'G', 'B'}

for i in range(n-1):
    for j in range(i+1, n):
        if j - i + j < n:
            # 順番が関係しない() or {}
            if {s[i], s[j], s[j-i+j]} == rgb:
                ans -= 1

print(ans)
