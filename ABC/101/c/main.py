import math

N, K = map(int, input().split())
A = list(map(int, input().split()))
min_index = A.index(1)

answer = math.ceil(min_index/(K-1)) + math.ceil((N-min_index-1)/(K-1))
print(answer)
