a, b = map(int, input().split())

# 掛け算なら中の要素の比較可能
print('Impossible' if a*b*(a+b) % 3 else 'Possible')
