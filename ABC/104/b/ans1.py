S = list(input())

bl = S[0] == 'A'
bl &= ('C' in S[2:-1])

if bl:
    S.remove('A')
    S.remove('C')

bl &= all(x in 'abcdefghijkrmnopqlstuvwxyz' for x in S)

answer = 'AC' if bl else 'WA'
print(answer)
