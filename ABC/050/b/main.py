n = int(input())
T = list(map(int, input().split()))
tt = T.copy()
m = int(input())

for i in range(m):
    T = tt.copy()
    p, x = map(int, input().split())
    T[p-1] = x
    print(sum(T))
