# ===================== leetcode 13 ==============================
import string
from collections import Counter
from typing import List

# def romanToInt(s: str) -> int:  # III
#     r_str = 'IVXLCDM'
#     r_list = [1, 5, 10, 50, 100, 500, 1000]
#     result = 0
#     for i in range(1, len(s)):
#         # if i == 0:
#         #     result += r_list[r_str.find(s[i])]
#         if r_str.find(s[i]) > r_str.find(s[i - 1]):
#             result += (r_list[r_str.find(s[i])] - r_list[r_str.find(s[i - 1])])
#         elif r_str.find(s[i]) <= r_str.find(s[i - 1]):
#             result += r_list[r_str.find(s[i - 1])]
#     if r_str.find(s[-1]) <= r_str.find(s[-2]):
#         result += r_list[r_str.find(s[-1])]
#     else:
#         result += r_list[r_str.find(s[-1])]
#     return result
#
#
# print(romanToInt(input('>>>> ')))


# ======================= leedcode 20 =======================

# def isValid(self, s: str) -> bool:
#     while '()' in s or '[]' in s or '{}' in s:
#         s = s.replace('()', '')
#         s = s.replace('[]', '')
#         s = s.replace("{}", '')
#     return True if len(s) == 0 else False


# ======================= leedcode 28 =========================

# def strStr(self, haystack: str, needle: str) -> int:
#     return haystack.find(needle)


# ==================== leedcode 58 ============================

# def lengthOfLastWord(s: str) -> int:
#     return len(s.split()[-1])
#
#
#
# print(lengthOfLastWord("Today is a nice day"))

# ====================== leedcode 125  =================================

# def isPalindrome(s: str) -> bool:
#     st1 = [i.lower() for i in s if i.isalnum()]
#     return st1 == st1[::-1]
#
#
# print(isPalindrome('0P'))
# print(isPalindrome('A man, a plan, a canal: Panama'))


# ==================== leedcode 242 ==========================

# strs = ["flower","flower","flower","flower"]


# def longestCommonPrefix(strs: list) -> str:
#     num = len(min(strs, key=len))
#     result = ''
#     for i in range(num):
#         temp = ''
#         for word in strs:
#             temp += word[i]
#         if len(set(temp)) == 1:
#             result += temp[0]
#         else:
#             break
#     return result
#
#
# print(longestCommonPrefix(strs))
# ================== leedcode 67 ==============================

# def addBinary(a: str, b: str) -> str:
#     s = int(a, 2) + int(b, 2)
#     return str(bin(s))[2:]
#
# print(addBinary('11', '1'))

# =================== ladecode alpha =========================

# from string import ascii_uppercase

# alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# print(alpha[27 % len(alpha)])
# num = int(input())
# result = ''
#
# if num <= 26:
#     print(alpha[len(alpha) % num])
# else:
#     print(False)


# ====================== leetcode 10 =================
# def isMatch(s: str, p: str) -> bool:
#     if s != p and '.' not in p and '*' not in p:
#         return False
#     elif
#
# print(isMatch('aa', 'a'))

# ==================== leetcode 205 =====================

# def isIsomorphic(s: str, t: str) -> bool:
#     my_dict = {}
#     for i in range(len(s)):
#         if  s[i] not in my_dict.keys() and t[i] not in my_dict.values():
#             my_dict[s[i]] = t[i]
#         elif my_dict.get(s[i]) != t[i]:
#             return False
#     return True
#
#
#     return True
#
#
#
# print(isIsomorphic('agg', 'add'))


# ================= leetcode 242 ===================

# def isAnagram(s: str, t: str) -> bool:
#     sl, tl = list(s), list(t)
#     return sorted(sl) ==  sorted(tl)
# s_dict = {}
# t_dict = {}
# for i in set(s):
#     s_dict[i] = s.count(i)
# for i in set(t):
#     t_dict[i] = t.count(i)
# if len(s_dict.keys()) != len(t_dict.keys()):
#     return False
# for i in s_dict.keys():
#     if s_dict.get(i) != t_dict.get(i):
#         return False
# return True


# print(isAnagram('rat', 'car'))
# print(isAnagram('ccca', 'ccac'))

# ================== leetcode 243 ====================

# def wordPattern(pattern: str, s: str) -> bool:
#     s = s.split()
#     res_dict = {}
#     for i in range(len(pattern)):
#         if not res_dict.get(pattern[i]):
#             if s[i] in res_dict.values():
#                 return False
#             res_dict[pattern[i]] = s[i]
#         else:
#             if res_dict[pattern[i]] != s[i]:
#                 return False
#     else:
#         return True
#
#
# print(wordPattern('abba', 'dog dog  dog dog'))
# print(wordPattern('abba', 'dog cat  cat fish'))

# ==================== leetcode 344 ===================

#
# def reverseString(s: list) -> None:
#     """
#     Do not return anything, modify s in-place instead.
#     """
#     left, right = 0, len(s) - 1
#     while left < right:
#         s[left], s[right] = s[right], s[left]
#         left += 1
#         right -= 1
#
#
# print(reverseString(["h", "e", "l", "l", "o"]))

# =================== leetcode 415 ================

# def addStrings(num1: str, num2: str) -> str:
#     max_num = max(len(num1), len(num2))
#     num1, num2 = num1.rjust(max_num, '0'), num2.rjust(max_num, '0')
#     q = 0
#     temp = ''
#     for i in range(max_num - 1, -1, -1):
#         number = int(num1[i]) + int(num2[i]) + q
#         if number > 9:
#             temp = str(number)[1] + temp
#             q = int(str(number)[0])
#             continue
#         temp = str(number)[0] + temp
#         q = 0
#     temp = str(q) + temp if q > 0 else temp
#
#     return temp
#
#
# print(addStrings('94', '11'))


# ======================= Array 26 ====================

# def plusOne(digits: list) -> list:
#     t = ''
#     for i in digits:
#         t += str(i)
#     t = str(int(t) + 1)
#
#     return [int(i) for i in t]
#
#
# print(plusOne([9, 9]))


#  ======================== 1 Two Sum ======================
# def twoSum( nums: List[int], target: int) -> List[int]:
#     result = 0
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 result = [i, j]
#     return result
#
# print(twoSum([3,3], 6))


# ========================= 459 ============================

# def repeatedSubstringPattern(s: str) -> bool:
#     for i in range(1, len(s) // 2 + 1):
#         re = not len(s) % i
#         res = s[:i]
#         if re and s == res * (len(s) // len(res)):
#             return True
#     return False
#
#
# print(repeatedSubstringPattern('aaaaaaaaaaa'))

# ====================== 482 =========================

# def licenseKeyFormatting(s: str, k: int):
#     s = s.replace('-', '')
#     q = len(s) % k
#     st = [s[:q]]
#     s = s[q:]
#     while len(s) != 0:
#         st.append(s[:k])
#         s = s[k:]
#     return '-'.join(st).strip('-')
#
#
# print(licenseKeyFormatting("2-4A0r7-4k", 4))

# ================== 1832 =======================


# def checkIfPangram(sentence: str) -> bool:
#     return len(set(sentence)) == 26
#
# print(checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))


# =============== 771 ==========================

# def numJewelsInStones(jewels: str, stones: str) -> int:
#     return sum([1 for i in stones if i in jewels])
#
#
# print(numJewelsInStones('aA', 'aAAbbbb'))

# ================= 1365 =====================

# def smallerNumbersThanCurrent(nums: List[int]) -> List[int]:
#     return [len([j for j in nums if nums[i] > j]) for i in range(len(nums))]
#
#
# print(smallerNumbersThanCurrent([8, 1, 2, 2, 3]))

# =================== 2325 ======================

# def decodeMessage(key: str, message: str) -> str:
#     st = 'abcdefghijklmnopqrstuvwxyz'
#     index = 0
#     my_dict = {}
#     for i in key:
#         if i.isalpha() and not i in my_dict:
#             my_dict[i] = st[index]
#             index += 1
#
#     return ''.join([my_dict.get(i, ' ') for i in message])
#
#
# print(decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"))


# ================== 268 =================

# def missingNumber(nums: List[int]) -> int:
#     summa = sum(list(range(0, max(nums) + 1)))
#     if summa != sum(nums) and 0 in nums:
#         return summa - sum(nums)
#     return max(nums) + 1 if 0 in nums and len(nums) != 0 else 0
#
#
# print(missingNumber([ 2]))

# ================== 350 =======================

# def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
#     d = {}
#
#
# print(intersect([1, 2, 2, 1], [2]))

# ================== 888 ======================

# def fairCandySwap(aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
#     s = (sum(aliceSizes) - sum(bobSizes)) // 2
#     for i in bobSizes:
#         if s + i in aliceSizes:
#             return [s + i, i]
#
#
# print(fairCandySwap([4, 4], [10, 10]))

# =================== 2 Add Two Numbers ================


# class ListNode:
#     pass
#
#
# def addTwoNumbers(l1: list[ListNode], l2: list[int]) -> list[int]:
#     s = str(int(''.join([str(i) for i in l1[::-1]])) + int(''.join([str(i) for i in l2[::-1]])))
#     s = list(map(lambda x: int(x), s))
#     return s
#
#
# print(addTwoNumbers([2, 4, 3], [5, 6, 4]))


# ========================== Task 7 ============================

s = -2344500


# temp = str(s).split()[0][::-1]
# while True:
#     if temp[0] == '0':
#         temp = temp[1:]
#     else:
#         break
#
# if s > 0:
#     print(temp)
# else:
#     print(temp[-1] + temp[:-1])

# ================================ leet code 7 ===========================
# def reverse(x: int) -> int:
#     number = str(x).split()[0][::-1]
#     while True:
#         if number[0] == '0' and len(number) > 1:
#             number = number[1:]
#         else:
#             break
#     number = int(number) if x > 0 else int(number[-1] + number[:-1])
#     if number < (-2 ** 31) or number > 2 ** 31 - 1:
#         return 0
#
#     return number


# def reverse(x: int) -> int:
#     number = int(str(abs(x))[::-1]) * (1 if x > 0 else -1)
#     return 0 if number < (-2 ** 31) or number > 2 ** 31 - 1 else number
#
#
# print(reverse(-23400))


# =====================  500. Keyboard Row ======================
# def findWords(words: List[str]) -> List[str]:
# result = []
#     for i in words:
#         count = 0
#         if i[0].lower() in 'qwertyuiop':
#             for j in i:
#                 if j.lower() in 'qwertyuiop':
#                     count += 1
#             if count == len(i):
#                 result.append(i)
#         if i[0].lower() in 'asdfghjkl':
#             for j in i:
#                 if j.lower() in 'asdfghjkl':
#                     count += 1
#             if count == len(i):
#                 result.append(i)
#         if i[0].lower() in 'zxcvbnm':
#             for j in i:
#                 if j.lower() in 'zxcvbnm':
#                     count += 1
#             if count == len(i):
#                 result.append(i)
#     return result
#
#
# print(findWords(["Hello", "Alaska", "Dad", "Peace"]))


# ==================== Detect Capital ========================

# def detectCapitalUse(word: str) -> bool:
#     if word == word.lower() or word == word.upper() or (word[0].isupper() and word[1:] == word[1:].lower()):
#         return True
#     return False
#
#
# print(detectCapitalUse("USE"))
# print(detectCapitalUse("leetcode"))
# print(detectCapitalUse("Google"))
# print(detectCapitalUse("g"))
# print(detectCapitalUse("FlaG"))


# ====================== 409 longest Palindrome =========================

# def longestPalindrome(s: str) -> int:
#     d = {}.fromkeys(set(s.lower()), 0)
#     for i in s:
#         d[i] = d.get(i) + 1
#     result = sum([i if not i % 2 else i - 1 for i in list(d.values())])
#     return result if len(set(s)) == 1 and len(s) % 2 == 0 or not result % 2 else result + 1
#
#
# print(longestPalindrome('tattarrattat'))


# ==================================

# def isValid(word: str) -> bool:
#     count_n, count_u, count_l, count_un, count_ud = 0, 0, 0, 0, 0
#     for char in word:
#         if char == ' ' and len(word) < 3:
#             return False
#         if char.isdigit():
#             count_n += 1
#         # if char.isupper():
#         #     count_u += 1
#         # if char.islower():
#         #     count_l += 1
#         if char.lower() in 'aoiuye':
#             count_un += 1
#         if char.lower() in 'bcdfghjklmnpqrstvwxyz':
#             count_ud += 1
#     counts = [count_n, count_un, count_ud]
#     if count_n >= 1 and (count_un >= 1 or count_ud >= 1):
#         return True
#
#     return False
#
#
# print(isValid('3pp'))


# ========================================================

# def minCostClimbingStairs(cost: List[int]) -> int:
#     result = []
#     i = 0
#     while len(cost) - 1 >= i:
#         # number = sum(cost[i: i + 3]) - max(cost[i:i + 3])
#         result.append(cost[i:i + 3])
#         if max(cost[i + 1: i + 3]) == i + 1 or max(cost[i + 1: i + 3]) != min(cost[i + 1: i + 3]):
#             i += 2
#         else:
#             i += cost.index(max(cost[i + 2:i + 3]))
#     summa = sum(result[0]) - max(result[0])
#     for i in range(len(result)):
#         c = max(result[i])
#         if c == 0:
#             summa += result[2]
#         elif c == 1:
#             summa += result[2]
#         elif c == 2:
#             summa += result[1]
#     return summa
#
#
# i = 0
# cost = [1,100,1,1,1,100,1,1,100,1]
# number = sum(cost[: i + 3]) - max(cost[:i + 3])
# print(minCostClimbingStairs(cost))

# ============================= 2076 =============================

# def buyChoco(prices: List[int], money: int) -> int:
#     summa = sum(sorted(prices)[:2])
#     if summa <= money:
#         return money - summa
#     return money
#
#
# print(buyChoco([1, 2, 2], 3))

# ====================================

# def findErrorNums(nums: List[int]) -> List[int]:
#     duplicate = sum(nums) - sum(set(nums))
#     num_max = max(nums)
#     result = sum((list(range(1, num_max + 1)))) - sum(set(nums))
#     num = num_max + 1 if result == 0 else result
#
#     return [duplicate, num]
#
#
# print(findErrorNums([1, 3, 1, 2]))
# print(findErrorNums([8,7,3,5,3,6,1,4]))

# ============================================

# def findTheArrayConcVal(nums: List[int]) -> int:
#     summa = 0
#     for i in range(len(nums) // 2):
#         summa += int(str(nums[i]) + str(nums[-(i + 1)]))
#     if len(nums) % 2:
#         summa += nums[len(nums) // 2]
#
#     return summa
#
#
# print(findTheArrayConcVal([7, 52, 2, 4]))
# print(findTheArrayConcVal([5, 14, 13, 8, 12]))


# =========================== 704

# def search(nums: List[int], target: int) -> int:
#     count = 0
#     low = 0
#     mid = len(nums) // 2
#     low =
#     for i in

# ============================== 496


# def nextGreaterElement( nums1: List[int], nums2: List[int]) -> List[int]:
#     result = []
#     nums2.append(0)
#     for i in nums1:
#         c = nums2.index(i)
#         if i < nums2[c + 1]:
#             result.append(nums2[c + 1])
#         else:
#             result.append(-1)
#     return result
#
#
# print(nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))


# ==================== 2913
# s = [1,2,1]
#
#
# def sumCounts(self, nums: List[int]) -> int:
#     result = 0
#     for i in range(len(nums)):
#         temp = set()
#         for j in range(i, len(nums)):
#             temp.add(nums[j])
#             result += len(temp) ** 2
#     return result

# ====================== 1897

# def makeEqual(words: List[str]) -> bool:
#     temp = ''
#     for i in words:
#         if len(i) > len(temp):
#             temp = i
#     _dict = dict().fromkeys(set(temp), 0)
#     for i in words:
#         for j in i:
#             _dict[j] = _dict.get(j) + 1
#
#     return max(_dict.values()) == min(_dict.values())
#
#
# print(makeEqual(["aabc", "aaaabc", "bc"]))
# print(makeEqual(["ab","a"]))


# ================================== 2363

# def mergeSimilarItems(items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
#     result = []
#     if len(items1) >= len(items2):
#         for i in range(len(items1)):
#             for j in range(len(items2)):
#                 if items1[i][0] == items2[j][0]:
#                     result.append([items1[i][0], items1[i][1] + items2[j][1]])
#                     break
#             else:
#                 result.append(items1[i])
#     else:
#         for i in range(len(items2)):
#             for j in range(len(items1)):
#                 if items2[i][0] == items1[j][0]:
#                     result.append([items2[i][0], items2[i][1] + items1[j][1]])
#                     break
#             else:
#                 result.append(items2[i])
#     return sorted(result, key=lambda x: x[0])
#
#
# print(mergeSimilarItems([[1, 3], [2, 2]], [[7, 1], [2, 2], [1, 4]]))

# =========================== 2540

# def secondHighest( s: str) -> int:
#     s = [int(i) for i in s if i.isdigit()]
#     s = sorted(set(s))
#     return s[-2] if s else -1

# ========================= 1287


# def findSpecialInteger(arr: List[int]) -> int:
#     temp = {}.fromkeys(set(arr), 0)
#     for i in arr:
#         temp[i] = temp.get(i) + 1
#     result = tuple(temp.values()).index(max(temp.values()))
#
#     return tuple(temp.keys())[result]
#
#
# print(findSpecialInteger([1, 2, 2, 6, 6, 6, 6, 7, 10]))


# ===================== 1512

# def numIdenticalPairs(nums: List[int]) -> int:
#     count = 0
#     for i in range(len(nums) - 1):
#         for j in nums[i + 1:]:
#             if nums[i] == j:
#                 count += 1
#     return count
#
#
# print(numIdenticalPairs([1, 2, 3, 1, 1, 3]))
# print(numIdenticalPairs([1,1,1,1]))

# ================ 1608

# def specialArray(nums: List[int]) -> int:
#     nums = tuple(i for i in nums if i != 0)
#     resutl = tuple(1 for i in nums if i >= len(nums))
#
#     return sum(resutl) if resutl else -1
#
#     # return sum(result) if sum(result) != 0 else -1
#
#
# print(specialArray([3, 5]))
# print(specialArray([0, 0]))
# print(specialArray([0, 4, 3, 0, 4]))

## chala

# ======================= 3

# def lengthOfLongestSubstring(s: str) -> int:
#     temp = ''
#     for i in range(len(s) - 1):
#         if s[i] != s[i + 1]:
#             temp += s[i]
#         else:
#
#
#     return temp  # ,len(set(temp))
#
#
# print(lengthOfLongestSubstring('abcabcbb'))
# print(lengthOfLongestSubstring('pwwkew'))
# print(lengthOfLongestSubstring('aadfg'))


# ==================  26

# def removeDuplicates(nums: List[int]) -> int:
#     i = 0
#     for i in range(len(nums)):
#
# nums = list(range(nums[0], nums[-1] + 1))
# return len(nums)
# # return nums[-1] if nums[0] != 0 else nums[-1] + 1


# print(removeDuplicates([1, 1, 2]))
# print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))


# ===================== 704

# def search(nums: List[int], target: int) -> int:
#     l = 0
#     h = len(nums) - 1
#     while l <= h:
#         mid = (l + h) // 2
#         if nums[mid] == target:
#             return mid
#         if nums[mid] > target:
#             h = mid - 1
#         else:
#             h = mid + 1
#     else:
#         return -1
#
#
# print(search([-1, 0, 3, 5, 9, 12], 9))


# =============================== 3136

# def isValid(word: str) -> bool:
#     word_u, word_un, number = 0, 0, 0
#     for i in word:
#         if i in 'aoiue':
#             word_u += 1
#         if i in 'bcdfghjklmnpqrstvwxyz':
#             word_un += 1
#         if i in '1234567890':
#             number += 1
#     if number > 1 and word_un > 1 and word_u > 1 and len(word) > 3:
#         return True
#     return False

# ============================== 1417
#
# def reformat(s: str) -> str:
#     st = ''
#     num = ''
#     for i in s:
#         if i.isdigit():
#             num += i
#         if i.isalpha():
#             st += i
#     if len(st) == 0 or len(num) == 0:
#         return ''
#     temp = ''
#     if len(st) > len(num):
#         temp = st[-1]
#         st = st[:-1]
#         for i in range(len(st)):
#             temp += num[i] + st[i]
#     elif len(num) > len(st):
#         temp = num[-1]
#         num = num[:-1]
#         for i in range(len(st)):
#             temp += st[i] + num[i]
#     elif len(st) == len(num):
#         for i in range(len(st)):
#             temp += num[i] + st[i]
#     return temp
#
#
# # print(reformat('a0b1c2'))
# print(reformat('covid2019'))
# # print(reformat('asdfghjk'))
# # print(reformat('123456789'))


# =========================  2224

# def convertTime(current: str, correct: str) -> int:
#     time = [list(map(int, current.split(':'))), list(map(int, correct.split(":")))]
#     result = time[1][0] - time[0][0]
#     second = time[1][1] - time[0][1]
#     n1 = second // 60
#     n2 = second % 60 // 15
#     n3 = second % 60 % 15 // 5
#     n4 = second % 60 % 15 % 5 // 1
#     result += n1 + n2 + n3 + n4
#
#     return result, second
#
#
# print(convertTime('02:30', '04:35'))
# print(convertTime('00:00', '23:35'))


# =======
# def minimumChairs( s: str) -> int:
#
#     if len(set(s)) == 1 and tuple(s)[0] == "E":
#         return len(s)
#     if len(set(s)) == 1 and tuple(s)[0] == "L":
#         return 0
#     count = 0
#     for i in range(len(s) - 1):
#         if s[i] == "E" and s[i+1] == 'L':
#             count += 1
#         if s[i] == "L" and s[i+1] == 'E':
#             count -= 1
#         if s[i] == "E" and s[i+1] == 'E':
#             count += 1
#     return count
#
# print(minimumChairs('EEEEEEE'))


# =========================


# def isLongPressedName(name: str, typed: str) -> bool:
#     d1 = {}.fromkeys(set(name), 0)
#     d2 = {}.fromkeys(set(typed), 0)
#     for i in name:
#         d1[i] = d1.get(i, 0) + 1
#     for i in typed:
#         d2[i] = d2.get(i, 0) + 1
#     for i in d1.keys():
#         if i not in d2.keys():
#             return False
#         if d1.get(i) > d2.get(i):
#             return False
#     return True
#
#
# print(isLongPressedName('alex', 'aaleex'))
# print(isLongPressedName('saeed', 'ssaaedd'))


# ======================


# def canBeTypedWords(text: str, brokenLetters: str) -> int:
#     return sum()
#
#
# print(canBeTypedWords("hello world", 'ad'))


# ====================

# def relativeSortArray(arr1: List[int], arr2: List[int]) -> List[int]:
#     result = arr1[:]
#     temp = []
#     for i in arr2:
#         for j in result:
#             if i == j:
#                 temp.append(j)
#                 arr1.remove(j)
#     arr1.sort()
#     return temp + arr1
#
#
# print(relativeSortArray([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]))
#
# def moveZeroes(nums: List[int]) -> None:
#     n = [i for i in nums if i != 0]
#     nums = n + ([0] * (len(nums) - len(n)))
#     # s = nums.count(0)
#     # for i in range(s):
#     #     nums.remove(0)
#     # for i in range(s):
#     #     nums.append(0)
#     # return nums
#
#
# print(moveZeroes([0, 1, 0, 3, 12]))

# ============================

# def longestValidParentheses(s: str) -> int:
#     def countt(st):
#         temp = st
#         while '()' in st:
#             st = st.replace('()', '')
#         return f"{st}{len(temp) - len(st)}"
#
#     temp = ''
#     i = 0
#     while i != len(s):
#         if s[i] == '(':
#             temp += s[i]
#             i += 1
#         elif temp and s[i] == ')' and '(' == temp[-1]:
#             temp += s[i] + ' '
#             i += 1
#         else:
#             i += 1
#     result = []
#     for i in temp.split():
#         result.append(countt(i))
#     # for number,
#     return result
#
#
# # print(longestValidParentheses(')()())'))
# # print(longestValidParentheses('(()(()()(())'))
# print(longestValidParentheses('()((())'))

# =================


# def getRow(rowIndex: int) -> List[int]:
#     result = [1] * rowIndex
#     if rowIndex == 1 and rowIndex == 2:
#         return result
#     result[1] = rowIndex - 1
#     result[-2] = rowIndex - 1
#     for i in range(2, len(result) // 2):
#         result[i] = result[i - 1] * 2
#         result[-i - 1] = result[i - 1] * 2
#     # return result
#     if len(result) % 2:
#         result[len(result)// 2] = (rowIndex - 1) ** 2
#     return result
#
#
#
#
# print(getRow(4))


# =========================

# def isCircularSentence( sentence: str) -> bool:
#     sentence = sentence.split()
#     for i in range(len(sentence) - 1):
#         if sentence[i][-1] != sentence[i + 1][0]:
#             return False
#     return True
#
# print(isCircularSentence("leetcode exercises sound delightful"))

# ======================

# def longestPalindrome(s: str) -> str:
#     if len(s) < 1:
#         return s
#     result = 0
#     temp = ''
#     for i in range(2, len(s)):
#         if s[:i] == s[:i][::-1] in s[::-1]:
#             if result < len(s[:i]):
#                 result = len(s[:i])
#                 temp = s[:i]
#     return temp
#
#
#
# print(longestPalindrome("cbbd"))


# =================
def minSteps(s: str, t: str) -> int:
    return sum((Counter(s) - Counter(t)).values())
    # d1 = {}.fromkeys(s, 0)
    # d2 = {}.fromkeys(t, 0)
    # for i in s:
    #     d1[i] = d1.get(i, 0) + 1
    # for i in s:
    #     d2[i] = d2.get(i, 0) + 1
    #
    # return list(d2.values()).count(0) + 1 if 0 in list(d2.values()) else 0


print(minSteps('leetcode', 'practice'))
print(minSteps('bab', 'aba'))
print(minSteps('anagram', 'mangaar'))

