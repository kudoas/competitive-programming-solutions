n, k = map(int, input().split())

n %= k
answer = min(n, abs(n-k))

print(answer)
