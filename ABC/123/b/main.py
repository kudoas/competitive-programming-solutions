A = [int(input()) for _ in range(5)]
B = [-(-a//10)*10-a for a in A]

print(sum(A)+sum(B)-max(B))
