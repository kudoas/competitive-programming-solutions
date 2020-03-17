n = int(input())
A = list(map(int, input().split()))

check = ''
ans = 0

for i in range(n-1):
    diff = A[i] - A[i+1]
    if check == '':
        if diff < 0:
            check = '+'
        elif diff > 0:
            check = '-'
    elif check != '':
        if check == '+' and diff > 0:
            ans += 1
            check = ''
        elif check == '-' and diff < 0:
            ans += 1
            check = ''

print(ans+1)
