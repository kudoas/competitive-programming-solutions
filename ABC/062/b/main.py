h, w = map(int, input().split())
ls = []

ls.append(['#']*(w+2))
for _ in range(h):
    ls.append(['#']+list(input())+['#'])
ls.append(['#']*(w+2))

for s in ls:
    print(*s, sep='')
