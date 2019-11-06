s, t = [input() for _ in range(2)]

# 文字列の比較可能
print('Yes' if sorted(s) < sorted(t, reverse=True) else 'No')
