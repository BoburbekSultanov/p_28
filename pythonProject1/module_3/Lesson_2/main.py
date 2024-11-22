# ============= Task 1 ================

# def plus_one(number):  # 1
#     return number + 1  # 4
#
#
# add_one = plus_one  # 2
# print(add_one(5))  # 3, # 5


# =============== Task 2 ===============


# def plus_one(number):  # 1
#     def add_one(number):  # 3
#         return number + 1  # 5
#
#     result = add_one(number)  # 4, # 6
#     return result  # 7
#
#
# print(plus_one(4))  # 2, # 8


# ============== Task 3 =======================

# def plus_one(number):  # 1
#     return number + 1  # 6
#
#
# def function_call(function):  # 2
#     number_to_add = 5  # 4
#     return function(number_to_add)  # 5
#
#
# print(function_call(plus_one))  # 3, # 7

# ============== Task 4 ===================

# def hello_function():  # 1
#     def say_hi():  # 3
#         return 'Hi'  # 6
#     return say_hi  # 4
#
#
# hello = hello_function()  # 2
# hello()  # 5

######################################################

# Dekoratorlarni yaratish .
#
# def uppercase_decorator(function): # 1
#     def wrapper(): # 4
#         func = function() # 7
#         make_uppercase = func.upper() # 9
#         return make_uppercase # 10
#
#     return wrapper # 5
#
# def say_hi(): # 2
#     return 'Hello there' # 8
#
# decorate = uppercase_decorator(say_hi) # 3
# decorate() # 6


# ===============================================================


# def plus_one(number):  # 1
#     return number + 1  # 4
#
#
# add_one = plus_one  # 2
# print(add_one(5))  # 3, # 5

# =================== Task 2 ===============================

# def plus_one(number):  # 1
#     def add_one(number):  # 3
#         return number + 1  # 5
#
#     result = add_one(number)  # 4
#     return result  # 6
#
#
# print(plus_one(4))  # 2 , # 7


# ====================== Task 3 =========================


# def plus_one(number):  # 2
#     return number + 1  # 6
#
#
# def function_call(function):  # 2
#     number_to_add = 5  # 4
#     return function(number_to_add)  # 5
#
#
# print(function_call(plus_one))  # 3, # 7


# ===================== Task 4 ===================
#
# def hello_function():  # 1
#     def say_hi(): # 3, # 6
#         return "Hi" # 7
#
#     return say_hi # 4
#
#
# hello = hello_function() # 2
# hello() # 5 , # 8

# ================ Task 5 ========================

# def uppercase_decorator(function):  # 1
#     def wrapper():  # 4
#         func = function()  # 8 , # 10
#         make_uppercase = func.upper()  # 11
#         return make_uppercase  # 12
#
#     return wrapper  # 5
#
#
# def say_hi():  # 2
#     return "hello there"  # 9
#
#
# decorate = uppercase_decorator(say_hi)  # 3, # 6
# decorate()  # 7 , # 13


# def kvadrat(function):
#     def wrapper(*args, **kwargs):
#         func = function(*args, **kwargs)
#         return func ** 2
#
#     return wrapper
#
#
# @kvadrat
# def add_num(num, num1):
#     return num + num1
#
#
# print(add_num(5, 1))


# def with_file(st=False):
#     def inner(function):
#         def wrapper(*args, **kwargs):
#             func = function(*args, **kwargs)
#             if st:
#                 with open('text.txt', 'w') as f:
#                     f.write(func)
#             else:
#                 return func
#         return wrapper
#     return inner


# @with_file()
# def temp():
#     return "Hello world"
#
#
# print(temp())

import calendar

print(calendar.calendar(2034))
