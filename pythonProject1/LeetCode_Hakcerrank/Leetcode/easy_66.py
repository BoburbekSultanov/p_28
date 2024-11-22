from typing import List


def plusOne(digits: List[int]) -> List[int]:
    return list((map(int, str(int(''.join(list(map(str, digits)))) + 1))))


print(plusOne([1, 2, 3, 9]))
