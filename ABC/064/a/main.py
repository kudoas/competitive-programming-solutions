# r, g, b = map(int, input().split())
# rgb = 100*r+10*g+b
# print('YES' if rgb % 4 == 0 else 'NO')

# これで3桁の数字として受け取れる
rgb = int(input()[::2])
print("NO" if rgb % 4 else "YES")
