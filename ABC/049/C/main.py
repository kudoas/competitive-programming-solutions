# s = input()[::-1]
# n = len(s)
# words = ['maerd', 'remaerd', 'esare', 'resare']
# while True:
#     if s[:5] == words[0]:
#         s = s[5:]
#         continue
#     elif s[:7] == words[1]:
#         s = s[7:]
#         continue
#     elif s[:5] == words[2]:
#         s = s[5:]
#         continue
#     elif s[:6] == words[3]:
#         s = s[6:]
#         continue
#     break
# print('NO' if s else 'YES')

s = input()
words = ['eraser',  'erase', 'dreamer', 'dream']
for w in words:
    s = s.replace(w, '')
print('NO' if s else 'YES')
