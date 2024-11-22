def make_fullname(first_name: str, last_name: str = '') -> str:
    return first_name + ' ' + last_name


#
# # f = make_fullname('Bobur', 'Sultanov')
# # print(f)
#
def str_slice(st: str, start: int, end: int, step: int = 1) -> str:
    t = ''
    for i in range(start, end, step):
        t += st[i]
    return t


#
# # print(str_slice('Hello', 0 , 3))
#
def my_pow(num1: int, num2: int) -> int:
    return num1 ** num2


# print(my_pow(2, 3))

def my_factorial(num: int) -> int:
    summa = 1
    for i in range(1, num + 1):
        summa *= i
    return summa


# print(my_factorial(int(input("Son kiriting: "))))

# def reverse_words(text: str) -> str:
#     return text[::-1]


def reverse_words(text: str) -> str:
    t = ''
    for i in range(len(text)):
        t = text[i] + t
    return bool(t == text)


#
# print(reverse_words('bobur'))


def make_sentance(*args: str) -> str:
    t = ''
    for i in args:
        t += i + ' '
    return t.strip()


# print(make_sentance('My', 'name', 'is', 'Botir'))


def make_tags(tag, word):
    return '<' + tag + '>' + word + '</' + tag + '>'


# print(make_tags('cite', 'Yay'))

def make_out_word(out, word):
    return out[:int(len(out) / 2)] + word + out[int(len(out) / 2):]


# print(make_out_word('[[]]', 'word'))

def combo_string(a, b):
    return (a + b) if len(a) == 0 or len(b) == 0 else b + a + b if len(a) > len(b) else a + b + a


# print(combo_string('aaa', 'b'))

def cat_dog(str):
    return bool(str.find('cat') or str.find('dog'))


# print(cat_dog('catdog'))

def count_code(str):
    count = 0
    for i in range(0, len(str) - 3):
        st = str[i:i + 4]
        if st[:2] == 'co' and st[-1] == 'e':
            count += 1
    return count


# print(count_code('aaacodebbbcope'))


def end_other(a, b):
    a, b = a.lower(), b.lower()
    c = bool(len(a) > len(b))
    return True if c and a.endswith(b) else True if not c and b.endswith(a) else False


# print(end_other('Hiabc', 'abc'))  # True
# print(end_other('AbC', 'HiaBc'))  # True
# print(end_other('abc', 'abXabc'))  # true
# print(end_other('Hiabc', 'abcd'))  # Fase
# print(end_other('Hiabc', 'bc'))  # True

def xyz_there(str):
    str = str.replace('.xyz', '')
    x = str.find('.xyz')
    x1 = str.find('xyz')
    count = str.count('xyz')
    return True if count > 1 else False if x >= 0 else True if x1 >= 0 else False


print(xyz_there('abcxyz'))  # → True
print(xyz_there('abc.xyz'))  # → False
print(xyz_there('xyz.abc'))  # → True
