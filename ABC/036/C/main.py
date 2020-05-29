n = int(input())
A = [int(input()) for _ in range(n)]
se = set(A)
li = sorted(se)
check = {x: i for i, x in enumerate(li)}
for a in A:
    print(check[a])
