def reverseVowels(s: str) -> str:
    s = list(s)
    temp = ''
    for i in s:
        if i.lower() in 'aeuio':
            temp += i
    temp = temp[::-1]
    i = 0
    j = 0
    while i != len(temp):
        if s[j].lower() in 'aeuio':
            s[j] = temp[i]
            i += 1
        j += 1

    return ''.join(s)


print(reverseVowels('IceCreAm'))
