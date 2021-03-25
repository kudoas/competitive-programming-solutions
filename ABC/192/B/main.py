S = input()

for i in range(len(S)):
    if i % 2 == 0 and S[i].islower():
        continue
    elif i % 2 == 1 and S[i].isupper():
        continue
    print('No')
    exit()
else:
    print('Yes')
