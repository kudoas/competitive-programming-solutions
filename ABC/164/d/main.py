s = input()
n = len(s)

cnt = 0
for i in range(n):
    for j in range(i+1, n+1):
        if j - i < 4:
            continue
        num = int(s[i:j])
        if num % 2019 == 0:
            cnt += 1

print(cnt)
