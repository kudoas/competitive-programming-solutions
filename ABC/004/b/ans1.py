m = [input()[::-1] for _ in range(4)][::-1]
print(*(row for row in m), sep='\n')
