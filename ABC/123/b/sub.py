ls = [int(input()) for _ in range(5)]
ans = 0
num = []

for i in ls:
    ans += -(-i//10)*10
    if str(i)[-1] != '0':
        num.append(str(i)[-1])

if num:
    print(ans-10+min([int(i) for i in num]))
else:
    print(ans)
