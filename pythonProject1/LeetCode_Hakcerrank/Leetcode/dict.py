from typing import List

roman = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


# ================== 169 Majority Element =================
# def majorityElement(nums: list) -> int:
#     d = {}
#     max1 = 0
#     for i in nums:
#         d[i] = d.get(i, 0) + 1
#         if max1 < d[i]:
#             max1 = d.get(i, d[i])
#     keys = list(d.keys())
#     values = list(d.values())
#     return keys[values.index(max1)]
#
#
# print(majorityElement([6, 5, 5]))


# ===================== 202. Happy Number =============================

# def isHappy(n: int) -> bool:
#     if n == 2 or n == 3:
#         return False
#     d = {}
#     i = 0
#     while i <= 10:
#         number = sum([int(i) ** 2 for i in str(n)])
#         d[n] = number
#         n = number
#         if number == 1:
#             break
#         i += 1
#     else:
#         return False
#
#     return False if min(list(d.values())) != 1 else True
#
#
# print(isHappy(1111111))


# =================== 217. Contains Duplicate =========================

# def containsDuplicate( nums: List[int]) -> bool:
#     return len(nums) != len(set(nums))


# ==================== 219. Contains Duplicate II =====================

# def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
#     i = 0
#     while i < len(nums):
#         print(nums[i:])
#         i += 1
#
#
# containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2)
