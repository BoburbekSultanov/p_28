from itertools import combinations
from typing import List


def subsetXORSum(nums: List[int]) -> int:
    temp = []
    for i in range(1, len(nums) + 1):
        temp.append(combinations(nums))


print(subsetXORSum([3, 4, 5, 6, 7, 8]))
