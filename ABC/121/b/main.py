n, m, c = map(int, input().split())
B = list(map(int, input().split()))

num = 0

for _ in range(n):
    A = list(map(int, input().split()))
    ans = [a*b for (a, b) in zip(A, B)]
    if sum(ans)+c > 0:
        num += 1

print(num)
