N = int(input())
S = list(input())
alphabet = [chr(ord('a') + i) for i in range(26)]

for s in S:
    ((alphabet.index(s))+26) % N
