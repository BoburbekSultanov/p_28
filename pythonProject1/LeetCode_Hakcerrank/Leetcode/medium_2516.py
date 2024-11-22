# def takeCharacters(s: str, k: int) -> int:
#     if len(set(s)) != 3:
#         return -1
#     i = 0
#     count = 0
#     temp = ''
#     minut = 0
#     while s:
#         temp += f'{s[i:k]}' + f'{s[-k:]}'
#         s = s[k:-k]
#         if len(set(temp)) == 3:
#             temp = ''
#             count += 1
#             minut += k
#         else:
#             minut += k
#         if count == 2:
#             return minut - k
#         else:
#             minut += k
#     return -1
#
#
# print(takeCharacters('bac', k=3))
# print(takeCharacters('a', k=1))
#


#
# def validPalindrome(s: str) -> bool:
#     i = 0
#     j = len(s) - 1
#     while i <= j:
#         if s[i] != s[j]:
#             temp = tuple(s[:i] + s[i + 1:])
#             temp1 = tuple(s[:j] + s[j + 1:])
#             return temp == temp[::-1] or temp1 == temp1[::-1]
#         i += 1
#         j -= 1
#     return True
#
# print(validPalindrome('cbbcc'))


# def checkRecord(s: str) -> bool:
#     p = 0
#     l = 0
#     for i in s:
#         if "P" == i:
#             p += 1
#             if p > 2:
#                 return False
#         if 'L' == i:
#             l += 1
#             if l >= 3:
#                 return False
#         if 'A' == i:
#             p = 0
#             l = 0
#     return True
#
# print(checkRecord('PPALLP'))
# print(checkRecord('PPALLL'))


# def makeFancyString(s: str) -> str:
#     temp = ''
#     for char in s:
#         if temp[-2:] == char + char:
#             continue
#         temp += char
#     return temp
#
# print(makeFancyString('leeetcode'))
# print(makeFancyString('aaabaaaa'))


# def findTheDifference(s: str, t: str) -> str:
#     s1 = s
#     t1 = t
#     s = {}.fromkeys(s, 0)
#     t = {}.fromkeys(t, 0)
#     for i in s1:
#         s[i] = s.get(i, 0) + 1
#     for i in t1:
#         t[i] = t.get(i, 0) + 1
#
#     for i in t:
#         if s.get(i) != t.get(i):
#             return i
#
#
# print(findTheDifference('a', 'aa'))
from collections import Counter
from itertools import chain, count
from sys import api_version
from typing import List, Optional

# def isSubsequence(s: str, t: str) -> bool:
#     i, j = 0, 0
#     while i < len(s) and j < len(t):
#         if s[i] == t[j]:
#             i += 1
#         j += 1
#     return i == len(s)
#
#
# print(isSubsequence('leeeeetcode', 'tmp'))

# from collections import Counter
#
#
# def maxCount(banned: List[int], n: int, maxSum: int) -> int:
#     ls = Counter(list(range(1, n + 1)))
#     banned = Counter(banned)
#     result = list((ls - banned).elements())
#     result.sort()
#     summa = 0
#     count = 0
#     for i in result:
#         if summa + i <= maxSum:
#             summa += i
#             count += 1
#         else:
#             return count
#     return count
#
#
# print(maxCount([1, 2, 3, 4, 5, 6, 7], 8, 1))
# print(maxCount([1,6,5], 5, 6))
# print(maxCount([11], 7, 50))


# def minCostClimbingStairs(cost: List[int]) -> int:
#     if not cost:
#         return 0
#     dp = [0] * len(cost)
#     dp[0] = cost[0]
#     if len(cost) >= 2:
#         dp[1] = cost[1]
#
#     for i in range(2, len(cost)):
#         t = cost[i]
#         t1 = dp[i - 1]
#         t2 = dp[i - 2]
#         re = min(t1, t2)
#         dp[i] = t + re
#
#     return min(dp[-1], dp[-2])
#
#
# print(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))

# def lengthOfLongestSubstring(s: str) -> int:
#     temp = ''
#     for i in range(len(s) - 1):
#         if s[i] != s[i + 1]:
#             temp += s[i]
#         else:
#             temp[i -1] = ''
#     return len(set(temp))
#
# print(lengthOfLongestSubstring('pwwkew'))
# print(lengthOfLongestSubstring('abcabcbb'))


# def findJudge(n: int, trust: List[List[int]]) -> int:
#     re1 = []
#     re2 = []
#     for i in trust:
#         re1.append(i[0])
#         re2.append(i[1])
#     if set(re2).difference(re1):
#         judge = max(re2, key = lambda x: re2.count(x))
#         if judge
#
#     return -1
#     # return re1, re2, list(re2)[0] if len(re2) == 1 else -1
#
#
# print(findJudge(2, [[1,2]])) #
# print(findJudge(3, [[1,3],[2,3]]))
# print(findJudge(3, [[1,3],[2,3], [3,1]]))
# print(findJudge(3, [[1,2],[2,3]]))
# print(findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]))
# print(findJudge(3, [[1,2],[2,3]]))


# def commonChars(words: List[str]) -> List[str]:
#     words[:] = [Counter(i) for i in words]
#
#
#
# print(commonChars(["bella", "label", "roller"]))
from math import factorial

from pythonProject1.module_3.Lesson_2.sendemail.send_messange import password


# def climbStairs(n: int) -> int:
#     # 1 1 2 3 5 8 13 21 34
#     res = [1] * (n+1)
#     for i in range(len(res) - 2):
#         res[i + 2] = res[i] + res[i + 1]
#     return res[-1]
#
#
# print(climbStairs(6))

# 5 -> [2, 2, 1] , [1, 1, 1, 1, 1], [2, 1, 1, 1]
# 4 - > [2, 2], [2, 1, 1], [1, 1, 1, 1]

# def validMountainArray(arr: List[int]) -> bool:
#     # if len(arr) != len(set(arr)) or len(arr) <= 2:
#     #     return False
#     if sorted(arr) == arr or sorted(arr, reverse=True) == arr:
#         return False
#     num_max = arr.index(max(arr))
#     if sorted(arr[:num_max + 1]) == arr[:num_max + 1] and sorted(arr[num_max:], reverse=True) == arr[num_max:]:
#         if len(arr[:num_max + 1]) != len(set(arr[:num_max + 1])) or len(arr[num_max:]) != len(set(arr[num_max:])):
#             return False
#         return True
#     return False
#
#
# print(validMountainArray([0,1,2,4,2,1]))
# print(validMountainArray([3, 5, 5]))
# print(validMountainArray([0, 3, 2, 1]))

# def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#     res = []
#     i = 0
#     j = 0
#     while i != m or j != n:
#         if nums1[i] != 0:
#             res.append(nums1[i])
#             i += 1
#         if nums2[j] != 0:
#             res.append(nums2[j])
#             j += 1
#     res.sort()
#     nums1[:] = res
#
# print(merge([1], 1, [], 0))


# def minimumBoxes(apple: List[int], capacity: List[int]) -> int:
#     s = sum(apple)
#     capacity[:] = sorted(capacity, reverse=True)
#     count, summa = 0, 0
#     while s > summa:
#             summa += capacity[count]
#             count += 1
#     return count
#
# print(minimumBoxes([1,3,2], [4,3,1,5,2]))

# # def triangleType(nums: List[int]) -> str:
# #     if sum(nums) // 3 == nums[0]:
# #         return 'equilateral'
# #     if nums[0] + nums[1] > nums[2] and nums[2] + nums[0] > nums[1] and nums[2] + nums[1] > nums[0]:
# #         if (nums[0] + nums[1] > nums[2]) or (nums[2] + nums[0] == nums[1]) or (nums[2] + nums[1] == nums[0]):
# #             return 'isosceles'
# #         return 'scalene'
# #     return None
#
#
#
#
# print(triangleType([9,4,9]))


# def missingInteger(nums: List[int]) -> int:
#     if len(nums) == 1:
#         return nums[0] + 1
#     summa = nums[0]
#     num = nums[0]
#     t = True
#     for i in range(1, len(nums)):
#         if num > nums[i]:
#             if summa not in nums:
#                 return summa
#             else:
#                 summa += 1
#                 t = False
#         else:
#             summa += nums[i]
#             num = nums[i]
#
#     return summa
#
# # print(missingInteger([1,2,3,2,5]))
# print(missingInteger([3,4,5,7,9,8,1,3,4,9]))


# def getRow(rowIndex: int) -> List[int]:
#     res = [1]
#     prev = 1
#     for k in range(1, rowIndex + 1):
#         next_val = prev * (rowIndex - k + 1) // k
#         res.append(next_val)
#         prev = next_val
#     return res
#
#
# print(getRow(2))
# print(getRow(3))
# print(getRow(4))
# print(getRow(5))
# print(getRow(6))
# print(getRow(7))
# print(getRow(8))

# def generate(numRows: int) -> List[List[int]]:
#     result = []
#     for i in range(1, numRows + 1):
#         res = [1]
#         prev = 1
#         for k in range(1, i):
#             next_val = prev * (i - k + 1) // k
#             res.append(next_val)
#             prev = next_val
#         result.append(res)
#     return result
#
# print(generate(5))

# def passThePillow(n: int, time: int) -> int:
#     result = 1
#     t = True
#     for i in range(time):
#         if t and  result != n:
#             result += 1
#         else:
#             if result == 1:
#                 t = True
#                 result += 1
#             else:
#                 t = False
#                 result -= 1
#     return result
#
#
# print(passThePillow(18, 38))
# print(passThePillow(4, 5))


