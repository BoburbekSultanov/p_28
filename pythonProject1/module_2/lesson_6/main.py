"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists
"""
from operator import is_not

# f = open("F:/pdp_academy/p_28/pythonProject1/module_2/lesson_6/users.txt", "x").close()
# f = open('users.txt', 'a')
# f.write('Hello world')
# f.close()
# f = open('users.txt', 'r')
# print(f.read())
# f = open('users.txt', 'w')
# f.write("Salom hammaga")
# f.close()
# f = open('users.txt', 'r')
# print(f.read())

# ========== task 1 ===================
# number = int(input("Enter number: "))
# file_path = input("Enter file path: ")
# for i in range(number):
#     f = open('users.txt', 'a')
#     f.write(data := input('Enter data: '))
#     f.close()
# f = open('users.txt', 'r')
# print(f.read())

# ================= task 2 =====================

# num = open('nums.txt', 'r')
# num = num.read()
# temp = []
# for i in list(num.split()):
#     if not int(i) % 2:
#         temp.append(i)
# data = ' '.join(temp)
# num = open('nums.txt', 'w')
# num.write(data)
# num.close()
# num = open('nums.txt', 'r')
# print(num.read())

# ==================== task 4 ======================

# text = open('F:/pdp_academy/p_28/pythonProject1/module_2/lesson_6/nums.txt', 'r')
# result = text.read().title()
# text = open('F:/pdp_academy/p_28/pythonProject1/module_2/lesson_6/nums.txt', 'w')
# text.write(result)
# text.close()


# f = open('nums.txt', 'r')
# print(f.read())
# f.close()

# f1 = open('F:/pdp_academy/p_28/pythonProject1/module_2/lesson_6/nums1.txt', 'x')
# f1.close()
f1 = open('nums1.txt', 'w')
f1.write('salom hammaga')
f1.close()
f1 = open('F:/pdp_academy/p_28/pythonProject1/module_2/lesson_6/nums1.txt', 'r')
print(f1.read())
f1.close()
