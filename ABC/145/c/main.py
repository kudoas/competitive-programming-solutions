import itertools
import math

n = int(input())
fac = math.factorial(n-1)

ll = [i for i in range(0, n)]
con = list(itertools.combinations(ll, 2))
cnt = len(con)

ls = []
for i in range(n):
    x, y = map(int, input().split())
    ls.append([x, y])

ans = []
for i, j in con:
    ans.append(((ls[i][0] - ls[j][0])**2 + (ls[i][1]-ls[j][1])**2)**0.5)

print(sum(ans)/(n/2))

