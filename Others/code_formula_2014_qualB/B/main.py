n = list(map(int, list(input())))
odd = n[::-1][1::2]
even = n[::-1][::2]
print(sum(odd), sum(even))
