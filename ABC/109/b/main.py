n = int(input())
W = [input() for _ in range(n)]

for i in range(n-1):
    if W[i][-1] != W[i+1][0] or W.count(W[i]) > 1:
        print('No')
        exit()

print('Yes')
