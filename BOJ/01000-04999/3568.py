s = input().replace(',', '')[:-1].split(' ')

for i in range(1, len(s)):
    s[i] = s[i].replace('[]', '][')

common = s[0]

for i in range(1, len(s)):
    print(common, end="")
    word = s[i]
    
    for idx in range(len(word)-1, 0, -1):
        c = word[idx]
        if not c.isalpha():
            print(c, end='')

    print('', end=' ')
    
    for idx in range(0, len(word)):
        if word[idx].isalpha():
            print(word[idx], end='')
    
    print(';')
