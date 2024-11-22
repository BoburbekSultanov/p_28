def reformat(s: str) -> str:
    if len(s) == 1:
        return s
    if s.isalpha() or s.isdigit():
        return ''
    st = ''.join([i for i in s if i.isdigit()])
    num = ''.join([i for i in s if i.isalpha()])
    if abs(len(st) - len(num)) > 1:
        return ''
    temp = ''
    if len(st) > len(num) and len(st) - len(num) == 1:
        for i in range(len(st) - 1):
            temp += st[i] + num[i]
        temp += st[-1]
    elif len(st) < len(num) and len(num) - len(st) == 1:
        for i in range(len(num) - 1):
            temp += num[i] + st[i]
        temp += num[-1]
    else:
        for i in range(len(st)):
            temp += st[i] + num[i]
    return temp


print(reformat('j'))
print(reformat('lkjhgfds'))
print(reformat('0987654321'))
print(reformat('09876kjhgf'))
