N, K = map(int, input().split())
H = [int(input()) for _ in range(N)]

H.sort()
minv = float('inf')

for i in range(N-K+1):
    minv = min(minv, H[i+K-1]-H[i])

print(minv)
