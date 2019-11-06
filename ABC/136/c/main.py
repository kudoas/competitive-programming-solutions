n = int(input())
H = list(map(int, input().split()))
cnt = 0

for i in reversed(range(0, n-1)):
    if H[i] > H[i+1]:
        H[i] -= 1
        if H[i] > H[i+1]:
            print('No')
            exit()

print('Yes')
