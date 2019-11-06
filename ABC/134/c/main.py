n = int(input())
ls = [int(input()) for _ in range(n)]
sls = sorted(ls)

for i in range(n):
    if sls[-1] == ls[i]:
        print(sls[-2])
    else:
        print(sls[-1])
