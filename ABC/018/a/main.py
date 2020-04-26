abc = [int(input()) for _ in range(3)]
s_abc = sorted(abc, reverse=True)

for i in abc:
    print(s_abc.index(i)+1)
