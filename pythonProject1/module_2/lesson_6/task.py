# ================= task 1 ===================================
from msvcrt import open_osfhandle
# while True:
#     num, num1 = map(int, input("Enter two numbers: ").split())
#     with open('nums1.txt', 'a') as f:
#         f.write(f"{num} + {num1} = {num + num1}" + '\n')
from operator import rshift

# ===================== task 2 ===========================

# for i in range(int(input('Son kiriting: '))):
#     if not i % 2:
#         with open('nums.txt', 'a') as f:
#             f.write(str(i) + ' ')

# ======================= task 3 ========================

# result = ''
# with open('nums.txt', 'r') as f:
#     for i in f.read().split():
#         if int(i) % 2:
#             result += i + ' '
# with open('nums.txt', 'w') as f:
#     f.write(result)

# ================== task 4 ============================

# with open('sample.txt') as f:
#     for i in f.read():
#         print(i, end='')


# ================ task 5 =============================

# with open('sample.txt') as f:
# for i in f.read().split():
#     if 'satr' in i:
#         print(i)

# ============== task 6 =============================

# result = ''
# with open('sample.txt') as f:
#     for i in f.read():
#         result += i
#
# with open('sample.txt', 'w') as f:
#     f.write(result.lower())

# =============== task 7 =====================

# open('F:/pdp_academy/p_28/pythonProject1/module_2/lesson_6/data.txt', 'x')
# name = input('Enter name: ').strip()
# age = input('Enter age: ').strip()
# with open('data.txt', 'a') as f:
#     f.write(f"{name},{age}\n")

# ============ task 8 =======================

# result = ''
# with open('data.txt') as f:
#     for i in f.read().split():
#         if int(i.split(',')[1]) > 25:
#             result += i + '\n'

# with open('filtered_data.txt', 'w') as f:
#     f.write(result)

# ============== task 9 =========================

# open('F:/pdp_academy/p_28/pythonProject1/module_2/lesson_6/students.txt', 'x')


# name = input('Enter name: ').strip().title()
# ball = input('Enter ball: ').strip()
# with open('students.txt', 'a') as f:
#     f.write(f"{name},{ball}\n")


# ======================== task 10 =============================

# result = ''
# with open('students.txt') as f:
#     for i in f.read().split():
#         if int(i.split(',')[1]) > 80:
#             result += i + '\n'
#
# with open('top_student.txt', 'a') as f:
#     f.write(result)

# ================ task 11 ==================================
# with open('students.txt') as f:
#     s = [int(i.split(',')[1]) for i in f.read().split()]
#     print(sum(s) / len(s))


# ================== task 12 =============================

# result = ''
# with open('students.txt') as f:
#     for i in f.read().split():
#         if i.split(',')[0] == 'Javohir':
#             i = 'Javohir,75\n'
#         result += i + '\n'
#
# with open('students.txt', 'w') as f:
#     f.write(result)


# ==================== task 13 =========================

# with open('students.txt') as f:
#     for i in f.read().split():
#         if i.split(',')[0] == 'Laylo':
#             print(i)


# =================== task 14 ========================


# result = ''
# with open('students.txt') as f:
#     s = [i for i in f.read().split()]
#     print(s)


# ========================== task 15 =====================

# open('F:/pdp_academy/p_28/pythonProject1/module_2/lesson_6/books.txt', 'x')

# book_name = input('Enter book name: ').strip().title()
# author_name = input('Enter ball: ').strip()
# with open('books.txt', 'a') as f:
#     f.write(f"{book_name},{author_name}\n")

# =============== task 16 ===========================

# result = ''
# with open('books.txt') as f:
#     for i in f.readlines():
#         if 'Robert C. Martin'.lower() in i.lower():
#             result += i
# with open('martin_books.txt', 'a') as f:
#     f.write(result)

# ================= task 17 =======================

# result = 0
# with open('books.txt') as f:
#     for i in f.readlines():
#         result += 1
# print(result)


# =============== task 18 ========================

# with open('books.txt') as f:
#     for i in f.readlines():
#         if 'Clean Code'.lower() in i.lower():
#             print(i.split(',')[1].title())


# ============= task 19 ==========================

