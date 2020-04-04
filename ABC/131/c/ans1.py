from fractions import gcd

a, b, c, d = map(int, input().split())

lcm = c * d // gcd(c, d)
a -= 1

under_b = b - (b//c + b//d - b//lcm)
under_a = a - (a//c + a//d - a//lcm)

answer = under_b - under_a
print(answer)
