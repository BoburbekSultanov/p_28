# def count_substring(string, sub_string):
#     result = 0
#     for i in range(len(string) - len(sub_string) + 1):
#         if string[i:len(sub_string) + i] == sub_string:
#             result += 1
#     return result
#
#
# print(count_substring('ABCDCDC', 'CDC'))
from itertools import count, permutations
from typing import List

# ==============================================
# s = input()
# print(s.isalnum(), not s.isalpha(), not s.isdigit(), not s.islower(), not s.isupper(), sep='\n')


# ================================================

# m = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
#
# n = int(input())
#
# def wrap(string, max_width):
#     f = 0
#     for i in range(len(string) // max_width):
#         s = ''
#         while max_width != len(s):
#             s += string[f]
#             f += 1
#         print(s)
#     return string[len(string) % max_width * -1:] if len(string) % max_width else ''
#
# print(wrap(m, n))


# =================================

# def print_formatted(number):
#     l = len(str(bin(number))) - 2
#     for i in range(1, number + 1):
#         print(str(i).rjust(l, ' '), str(oct(i))[2:].rjust(l, ' '), str(hex(i))[2:].rjust(l, ' '), str(bin(i))[2:].rjust(l, ' '))
#
#
# print_formatted(17)

# def findRelativeRanks(score: List[int]) -> List[str]:
#     result = ['_'] * len(score)
#     i = 1
#     r = True
#     while i != len(score) + 1:
#         s = max(score)
#         ind = score.index(s)
#         if r and i - 1 != 3:
#             y = ['Gold Medal', 'Silver Medal', 'Bronze Medal']
#             result[ind] = y[i -1]
#             score[ind] = 0
#         else:
#             r = False
#             result[ind] = f'{i}'
#             score[ind] = 0
#         i += 1
#     return result
#
#
# print(findRelativeRanks([4]))


# def findContentChildren(g: List[int], s: List[int]) -> int:
#     g.sort()
#     s.sort()
#     _r = min(len(g), len(s))
#     count = 0
#     i, j = 0, 0
#     for i in range(_r):
#         if g[i] <= s[i]:
#             count += 1
#             i += 1
#         j += 1
#
#     return count
#
#
# print(findContentChildren([10, 9, 8, 7], [5, 6, 7, 8]))
from itertools import groupby, combinations

# def findEvenNumbers(digits: List[int]) -> List[int]:
#     result = set()
#     for i, j, k in permutations(digits, 3):
#         if i != 0 and k % 2 == 0:
#             s = i * 100 + j * 10 + k
#             result.add(s)
#     return sorted(result)
#
#
# print(findEvenNumbers([2, 2, 8, 8, 2]))


# def specialArray(nums: List[int]) -> int:
#     nums.sort()
#     while nums.count(0):
#         nums.remove(0)
#     if not nums:
#         return -1
#     for i in range(1, len(nums) + 1):
#         count = 0
#         for j in nums:
#             if i <= j:
#                 count += 1
#         if count == i:
#             return count
#         else:
#             count = 0
#     return -1
#
#
# print(specialArray([0, 4, 4, 3, 0]))


# nums=sorted(nums)
# n=len(nums)
# for i in range(n,0,-1):
#     k=bisect.bisect_left(nums,i)
#     if(n-k==i):
#         return i
# return -1

from collections import Counter


def relativeSortArray(arr1: List[int], arr2: List[int]) -> List[int]:
    l1 = Counter(arr1)
    return l1


print(relativeSortArray([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]))
