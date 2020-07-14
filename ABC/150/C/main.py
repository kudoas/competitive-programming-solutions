from itertools import permutations

n = int(input())
N = [i for i in range(1, n+1)]
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
all = [p for p in permutations(N, n)]
ans = abs(all.index(P) - all.index(Q))
print(ans)
