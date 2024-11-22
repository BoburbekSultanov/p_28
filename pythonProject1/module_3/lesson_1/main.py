# products = ["Marker", "Pen", "Pencil", "Box", "Phone"]


# for
# iterator = iter(products)
# while True:
#         i = next(iterator)
#         print(i)
#

# def temp():
#     return 12
#
# print(temp())

# ============================= cycle =========================================

# def my_cycle(products):
#     while True:
#         for i in products:
#             yield i
#
#
# for i in my_cycle([1, 2, 3, 4, 5]):
#     print(i)

# ============================== count =======================================

# def my_count(start=0, step=1):
#     while True:
#         yield start
#         start += step
#
#
# for i in my_count(6, 4):
#     print(i)


# def my_repeat(start, step : int):
#     for _ in range(step):
#         yield start
#
#
# for i in my_repeat("salom", 10):
#     print(i)


# def my_accumulate(ls: list[int]):
#     # temp = ls[0]
#     # yield ls[0]
#     # for i in range(1, len(ls)):
#     #     yield temp + ls[i]
#     #     temp = temp + ls[i]
#     for i in range(len(ls)):
#         yield sum(ls[:i + 1])
#
#
# for i in my_accumulate([1, 2, 3, 4, 5, 6, 7, 8]):
#     print(i)


# def _batched(st: str, cut: int):
#     while len(st) > cut:
#         yield st[:cut]
#         st = st[cut:]
#     yield st
#
#
#
# for i in _batched('123456789', 4):
#     print(i)

# ========================================= chain ====================================

# def _chain(*args):
#     temp = ''
#     for i in args:  #
#         for j in i:
#             temp += str(j) + ' '
#     yield temp.strip()
#
#
# for i in _chain([1, 23, 'w', 6], [8, 9, 0, 0], [2, 'sd', 'sdd']):
#     print(i)


# count

# def m_count(start, step=1):
#     while True:
#         yield start
#         start += step
#
#
# for i in m_count(14, 100000 ):
#     print(i)

# ================ cycle =====================

# def _cycle(st):
#     while True:
#         for i in st:
#             yield i
#
#
# for i in _cycle("ASDFG"):
#     s = time.sleep(1)
#     print(i)
#
# c = 0
# s = True
# while s:
#     second = time.sleep(1)
#     for i in _cycle('asfdfg'):
#         print(i)
#         c += 1
#         if second == 1:
#             s = False

# ============= compress =======================================
# def my_compress(lists,iterable):
#     index = 0
#     for i in lists:
#         if i == 1:
#             yield iterable[index]
#             index += 1
#         else:
#             index +=1
#
# for i in my_compress([1,0,1,0,1,1],"ABCDEF"):
#     print(i,end=" ")

# ===========================  filterfalse ====================================
from itertools import groupby


# def my_filterfalse(x,iterable):
#     for i in iterable:
#         if x<=i:
#             yield i
#
#
# for j in my_filterfalse(5,[1,2,12,4,5,6,7]):
#     print(j)


# ===================== grupbby ==============================


# def my_grupby(iterable, function):
#     d = {}.fromkeys([len(i)] for i in iterable], [])
#
#
# for j in my_grupby(["A", "B", "DEF"], len):
#     print(j)


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
# def my_islice(iterable,step):
#         yield iterable[step:len(iterable)]
#
# for j in my_islice("ABCDEFG",4):
#     print(j)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# def my_pairwise(iterable):
#     for i in range(0,len(iterable)-1):
#         yield  iterable[i:i+2]
#
# for j in my_pairwise("ABCDEFG"):
#     print(j,end=" ")
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# def my_starmap(iterable):
#     for i in iterable:
#         yield i[0]**i[1]
#
# for j in my_starmap([(2,5),(3,4),(6,2)]):
#     print(j,end=" ")

# #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# def my_takewhile(iterable):
#     pass

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# def my_tee():
#     pass


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# def my_zip_longest(iterable , text):
#        i = 0
#        while i < len(iterable):
#            for j in range(0, len(text)):
#               if i <= j:
#                   yield iterable[i]+text[j]
#                   text.strip(text[j])
#                   iterable.strip(iterable[i])
#                   i +=1
#               elif i > j:
#                   yield iterable[i]+"-"
#                   iterable.strip(iterable[i])
#                   i+=1
# for a in my_zip_longest("ABCD","xy"):
#       print(a)


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# def my_product(iterable):
#     for i in range(0,len(iterable)-1):
#         for j in range(0,len(iterable)-1):
#            yield iterable[i]+iterable[j]
#
#
# for j in my_product("ABCDF"):
#     print(j,end=" ")
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# def my_permutations(iterable):
#     for i   in range(0,len(iterable)):
#         for j in range(0, len(iterable)):
#            if  iterable[i] != iterable[j]:
#               yield iterable[i]+iterable[j]
#
#
# for c in my_permutations("ABCD"):
#     print(c,end=" ")

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# a, b, c = map(int, input().split())
# if a < b:
#     a, b = b, a
# if b < c:
#     b, c = c, b
# if a < b:
#     a, b = b, a
# print(a - c)


# a, b, c = map(int, input().split())
# print(a-c) if b > c else print(a-b) if a > c else print(c-b) if a > b else print(b - a) if b > c else print(c - a) if a < c else print(b - c)






# 12000000000
# 12002320024200

