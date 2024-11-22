from typing import List


def mergeSimilarItems(items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
    res = []
    helper = [0]
    for arr in items1:
        helper[arr[0]] = arr[1]
    for arr in items2:
        if helper[arr[0]]:
            helper[arr[0]] += arr[1]
        else:
            helper[arr[0]] = arr[1]
    for i in range(1001):
        if helper[i]:
            res.append([i, helper[i]])

    return res


print(mergeSimilarItems([[1, 1], [4, 5], [3, 8]], [[3, 1], [1, 5]]))  # [[1,6],[3,9],[4,5]]
print(mergeSimilarItems([[1, 1], [3, 2], [2, 3]], [[2, 1], [3, 2], [1, 3]]))  # [[1,4],[2,4],[3,4]]
print(mergeSimilarItems([[1, 3], [2, 2]], [[7, 1], [2, 2], [1, 4]]))  # [[1,7],[2,4],[7,1]]
