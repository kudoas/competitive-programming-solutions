a, b, c = map(int, input().split())

# aの倍数のあまりはb+1種類ありでループする
print('YES' if any(a*i % b == c for i in range(1, b+1)) else 'NO')
