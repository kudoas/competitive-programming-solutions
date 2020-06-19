h = int(input())
cnt = 0
i = 1
while h != 1:
    h //= 2
    cnt += i
    i *= 2
print(cnt+i)
