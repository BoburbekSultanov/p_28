# l = ["Hello", 1, 10, "5.0", [1, 2, 3], {1, 23}, [5, 4, 7]]
# for i in l:
#     if type(i) == list:
#         print(*i, sep='\n')

# for i in l:
#     if type(i) == list:
#         for j in i:
#             if type(j) == int and j % 2 == 0:
#                 print(j, end = ' ')

# print(*[j for i in l if type(i) == list for j in i if type(j) == int and not j % 2])

# ls = range(1, 30)
# print(lst := [['juft', 'toq'][i % 2] for i in ls])


# nums = [1, 2, 1, 6, 5, 2, 2]
# print(sum(nums))


# for i in set(nums):
#     if result < nums.count(i):
#         result = i
# print(result := nums.sort(key=lambda x: nums.count(x)))
