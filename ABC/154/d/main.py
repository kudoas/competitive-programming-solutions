n, k = map(int, input().split())
pp = list(map(int, input().split()))

answer = sum(pp[:k])
total = sum(pp[:k])

for i in range(n-k):
    answer = max(answer, total - pp[i] + pp[i+k])

print((answer+k)/2)
