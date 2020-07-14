s = input()
for i in range(n := len(s)):
    for j in range(n-i):
        if s[:i]+s[i+j:] == "keyence":
            print('YES')
            exit()
else:
    print('NO')
