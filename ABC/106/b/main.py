n = int(input())
ans = 0

# 第一感
for i in range(1, n+1, 2):
    cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1
            if cnt == 8:
                ans += 1

print(ans)


# 約数生成関数の自作
def make_divisors(n):
    divisors = []

    # 数値を全部回さないのがミソ
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors
