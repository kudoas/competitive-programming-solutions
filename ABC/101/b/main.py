n = input()
cnt = 0

for i in n:
    i = int(i)
    cnt += i

print('Yes' if int(n) % cnt == 0 else 'No')
