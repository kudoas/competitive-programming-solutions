n = int(input())
A = list(map(int, input().split()))
print('YES' if n == len(set(A)) else 'NO')
