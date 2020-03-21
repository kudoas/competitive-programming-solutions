n, m = map(int, input().split())
x = list(map(int, input().split()))

if n >= len(x):
    print(0)
    exit()

ls = []
x.sort()

for i in range(m-1):
    diff = x[i+1] - x[i]
    ls.append(diff)

ls.sort(reverse=True)
ans = sum(ls)

for i in range(n-1):
    ans -= ls[i]

print(ans)
