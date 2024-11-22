# =============== task 1 ===================

def my_pow(num: float, step: float) -> float:
    return num ** step


# print(my_pow(5, 2))
# ============== task 2 ====================

def my_factorial(num: int) -> int:
    summa = 1
    for i in range(1, num + 1):
        summa *= i
    return summa


# print(my_factorial(int(input("Son kiriting: "))))

# ============== task 3 ====================

def reverse_words(text: str) -> str:
    t = ''
    for i in range(len(text)):
        t = text[i] + t
    return t


# print(reverse_words('bobur'))

# ============ task 4 ====================

def is_palindrome(words: str) -> bool:
    return bool(words[::-1] == words)


# print(is_palindrome("hello"))

# ================ task 5 ========================

def count_vowels_consonants(words: str) -> int:
    count = 0
    for i in words.lower():
        if i in 'aeiou':
            count += 1
    return count


# print(count_vowels_consonants('Assalom Uzbekiston'))

# ================ task 6 =======================

def count_unique_elements(words: str) -> int:
    count = 0
    for i in words:
        if not i.isalnum():
            count += 1
    return count


print(count_unique_elements("hello"))


# ================ hm 1 =========================

def password_check(password: str) -> bool:
    if len(password) < 8:
        return False
    count_lower = 0
    count_upper = 0
    count_number = 0
    for i in password:
        if i.islower() or i.isupper() or i.isdigit():
            count_lower += 1
            count_upper += 1
            count_number += 1
    if count_lower < 1 and count_upper < 1 and count_number < 1:
        return False
    return True


# print(password_check(input()))

# ================== hm 2 ==================================


def str_slicing(data, start, end, step):
    pass


'sa'.replace()

