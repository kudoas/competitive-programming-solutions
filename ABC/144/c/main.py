n = int(input())


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors


r = make_divisors(n)

if len(r) % 2 == 1:
    a = r[len(r)//2]
    print((a-1)+(a-1))
else:
    a = int(len(r)/2)
    print((r[a-1]-1)+(r[a]-1))
