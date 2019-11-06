n, k, q = map(int, input().split())

menber = [0]*n
if q-k >= 0:
    for i in range(q):
        ans = int(input())
        menber[ans-1] += 1
else:
    menber = [100000]*n

for j in menber:
    if j >＝ q-k:
        print('Yes')
    else:
        print('No')
