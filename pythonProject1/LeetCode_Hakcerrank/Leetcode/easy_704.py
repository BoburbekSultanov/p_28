from math import trunc
from typing import List
from unittest.mock import right


def search(nums: List[int], target: int) -> int:
    left = 0
    lost = len(nums) - 1
    mid = len(nums) // 2
    while True:
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            lost = mid - 1
            mid = (left + lost) // 2
        if nums[mid] < target:
            left = mid + 1
            mid = (left + lost) // 2


print(search([-1, 0, 3, 5, 9, 12], 9))
