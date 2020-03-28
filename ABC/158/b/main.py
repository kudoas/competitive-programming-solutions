n, a, b = map(int, input().split())

answer = n // (a+b) * a + min((n % (a+b)), a)
print(answer)
