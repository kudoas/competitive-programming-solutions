import math

n, k = map(int, input().split())
A = list(map(int, input().split()))

answer = math.ceil((n-1)/(k-1))
print(answer)
