from fractions import gcd

# cもしくはdで割れるの反対はcでもdでも割れない
a, b, c, d = map(int, input().split())


def f(n):
    x = n//c
    x += n//d
    lcm = c*d//gcd(c, d)
    x -= n//lcm
    return n-x


# aは答えに含めるのでa-1までを除外する
print(f(b)-f(a-1))
