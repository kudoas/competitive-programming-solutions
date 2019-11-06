n = int(input())
ls = list(map(int, input().split()))
menber = list(range(1, n+1))

dict1 = dict(zip(ls, menber))
dict1 = sorted(dict1.items(), key=lambda x: x[0])

for i in range(len(dict1)):
    print(dict1[i][1], end=' ')
