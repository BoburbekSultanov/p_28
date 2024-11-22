from collections import Counter
from tempfile import template
from typing import List


# def find_word(word: str) -> int:
#     result = 1
#     tmp = word[0]
#     for i in word[1:]:
#         if i == tmp:
#             result += 1
#         tmp = i
#     return result
#
#
#
#
# print(find_word('abbcccc'))
# print(find_word('asdfghjkll'))
# print(find_word('aaaa'))
# print(find_word('all'))
# print(find_word('aabb'))
# print(find_word('ere'))

# def removeTrailingZeros(num: str) -> str:
#     num = list(num)
#     while num[-1] == '0':
#         num.pop(-1)
#     return ''.join(num)
#
# print(removeTrailingZeros('51230100'))


# def summaryRanges(nums: List[int]) -> List[str]:
#     tmp = []
#     i = 0
#     while nums:
#         if nums[i] + 1 == nums[i + 1] and nums[i + 1] + 1 == nums[i + 2]:
#             tmp.append(f"{nums[i]}->{nums[i + 2]}")
#             nums = nums[3:]
#
#
#
# print(summaryRanges([0, 1, 2, 4, 5, 7]))  # ["0->2","4->5","7"]
# print(summaryRanges([0, 2, 3, 4, 6, 8, 9]))  # ["0","2->4","6","8->9"]


# def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
#     tmp = list(set(nums1).intersection(set(nums2)))
#     return tmp
#
#
#
# print(intersection([1, 2, 2, 1], [2, 2]))
# print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))
