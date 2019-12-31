n = int(input())
s = list(input())

print('Yes' if s[:n//2] == s[n//2:] else 'No')
