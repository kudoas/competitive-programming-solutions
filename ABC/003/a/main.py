n = int(input())

answer = 0
for i in range(1, n+1):
    answer += 10000*i*(1/n)

print(answer)
