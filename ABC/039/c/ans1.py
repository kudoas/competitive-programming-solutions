pattern = 'WBWBWWBWBWBW' * 10
ls = ['Do', '#', 'Re', '#', 'Mi', 'Fa', '#', 'So', '#', 'La', '#', 'Si']

S = input()

for i in range(12):
    if S == pattern[i:i+20]:
        answer = ls[i]
        break

print(answer)
