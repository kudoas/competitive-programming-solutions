n, X = map(int, input().split())
A = list(map(int, input().split()))
price = 0
j = 0

binary = bin(X)

for i in reversed(binary):
    if i == '1':
        price += A[j]
    if i == 'b':
        print(price)
        exit()
    j += 1
