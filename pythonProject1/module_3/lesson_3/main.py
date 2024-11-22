# st = input("Enter variable: ")
#
# st.isspace()
# def is_variable(st):
#     if len(st.split()) == 1 and not st[0].isdigit():
#         for char in st:
#             if char not in '!@#$%^&*()-=+{}[];"",.<>/?|':
#                 return True
#     return False
#
#
# print(input('Enter variable: ').isidentifier())
#
# from typing import List
#
#
# def checkIfExist(arr: List[int]) -> bool:
#     # temp = len(arr)
#     # for i in range(temp):
#     #     for j in range(temp):
#     #         if i != j and (arr[i] == arr[j] * 2):
#     #             return True
#     # return False
#     return True if arr.count(0)>1 else any(x for x in arr if 2*x in arr )
import calendar

# =================================================================

with open('calendar.txt', 'w') as f:
    f.write(calendar.calendar(2024))

