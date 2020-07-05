n = int(input())
A = [0]+list(map(int, input().split()))+[0]
dist = [0]*(n+1)
for i in range(n+1):
    dist[i] = abs(A[i]-A[i+1])
total = sum(dist)
for i in range(1, n+1):
    ans = total + abs(A[i-1]-A[i+1]) - (abs(A[i-1]-A[i])+abs(A[i]-A[i+1]))
    print(ans)
