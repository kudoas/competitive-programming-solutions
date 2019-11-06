k, n = map(int, input().split())

for i in range(n-k+1, n+k):
    print(i, end=' ')
