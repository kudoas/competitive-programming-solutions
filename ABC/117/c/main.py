N, M = map(int, input().split())
X = list(map(int, input().split()))

diff = []

for i in range(M-1):
    if X[i+1] < X[i]:
        num = (X[i+1] - X[i])*-1
        diff.append(num)
    else:
        diff.append(X[i+1] - X[i])

print(diff)

# for _ in range(N):
#     diff.remove(max(diff))

print(sum(diff))
