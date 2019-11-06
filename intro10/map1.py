l = [1, 2, 3, 4, 5]


def double(x):
    return x*2

# new_l = []
# for i in l:
#     new_l.append(double(i))


new_l = list(map(double, l))
print(new_l)
