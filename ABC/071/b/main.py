import string

se = set(list(input()))
alphabet = [s for s in string.ascii_lowercase]

for al in alphabet:
    if al not in se:
        print(al)
        exit()

print('None')
