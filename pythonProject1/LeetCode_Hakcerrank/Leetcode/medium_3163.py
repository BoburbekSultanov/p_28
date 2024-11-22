def compressedString(word: str) -> str:
    result = ''
    temp = []
    st = [word[0], 0]
    for char in word:
        if st[0] == char:
            st[1] += 1
        else:
            if st:
                temp.append(st)
                st = [char, 1]
    else:
        temp.append(st)
    for char, count in temp:
        if count <= 9:
            result += f'{count}{char}'
        else:
            result += (f'9{char}'* (count // 9) ) + (f'{count % 9}{char}' if count % 9 else '')

    return result


print(compressedString('aaaaaaaaaaaaaabb'))
print(compressedString('aadaa'))
