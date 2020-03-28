n = int(input())

buttons = [0] * 10**5

for i in range(n):
    buttons[i] = int(input())

next = 1
i = 0
while i <= 10**5:
    i += 1
    next = buttons[next-1]
    if next == 2:
        print(i)
        exit()

print(-1)
