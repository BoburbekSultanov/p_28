from typing import List


def threeConsecutiveOdds(arr: List[int]) -> bool:
    for i in range(len(arr) - 2):
        if arr[i] % 2 and arr[i + 1] % 2 and arr[i + 1] % 2:
            return False
    return True


print(threeConsecutiveOdds([102, 780, 919, 897, 901]))
