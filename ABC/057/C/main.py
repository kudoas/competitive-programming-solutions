n = int(input())
INF = 10**18
ans = INF


def f(a, b):
    return max(len(str(a)), len(str(b)))


for i in range(1, int(n**.5)+1):
    if n % i == 0:
        ans = min(f(i, n//i), ans)

print(ans)
