n = int(input())
X = list(map(int, input().split()))
sX = sorted(X)
median1 = sX[n//2-1]
median2 = sX[n//2]

for x in X:
    if x <= median1:
        print(median2)
    else:
        print(median1)
