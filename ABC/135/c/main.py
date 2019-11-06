n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
total = sum(A)

for i in range(n):
    b = max(B[i] - A[i], 0)
    A[i] = max(A[i]-B[i], 0)
    A[i+1] = max(A[i+1]-b, 0)

print(total-sum(A))
