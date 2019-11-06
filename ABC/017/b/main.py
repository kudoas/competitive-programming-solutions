S = input()
S = S.replace('ch', '_')

print('YES' if set(S) <= set('_oku') else 'NO')
