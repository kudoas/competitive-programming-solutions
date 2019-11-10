a, b = map(int, input().split())
s = input()
t = s[:a] + s[a+1:]
bl = (s[a] == '-') and ('-' not in t)
print('Yes' if bl else 'No')
