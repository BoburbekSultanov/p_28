# =============================== 124 ==========================

# n, ls, k = int(input()), list(map(int, input().split())), int(input())
# max1 = max(ls)
# for i in range(len(ls)):
#     if ls[i] == max1:
#         ls[i] = ls[k - 1]
# ls[k - 1] = max1
#
#
# print(*ls)

# =========================== 125 =================================

# n, ls = int(input()), list(map(int, input().split()))
# k, l = map(int, input().split())
# print(sum([i ** 3 for i in ls[k - 1: l]]))

# ===================== 126 ==================================
# from math import log
# n, ls = int(input()), list(map(int, input().split()))
# s = log(sum(ls)/ len(ls))
# print(*[f'{log(sum(ls)/ len(ls)) + 0.0001:.2f}' if i < 0 else f'{i:.2f}' for i in ls])

# ====================== 127 =============================

# n, ls = input(), list(map(int, input().split()))
# print(*[min(ls) ** 2 if i < 0 else i for i in ls])

# ======================= 128 =============================

# n, ls = input(), list(map(int, input().split()))
# print(f'{sum([i for i in ls if not i % 2]) / len([i for i in ls if not i % 2]):.2f}')


# ====================== 129 =================================

# n, ls = input(), list(map(int, input().split()))
# print(sum([i for i in ls if not i % 2 or not i % 3 or not i % 5]))

# ====================== 204 ================================

# n, ls, m = input(), list(map(int, input().split())), int(input())
# print(*[(s := map(int, input().split()), sum(ls[s[0] - 1: s[1]])) for i in range(m)], sep = '\n')

# n, ls, m = input(), list(map(int, input().split())), int(input())
# s = []
# for i in range(m):
#     l, k = map(int, input().split())
#     s.append(sum(ls[l - 1: k]))
# print(*s, sep='\n')

# ======================== 205 ==============================
# import numpy as np
#
# n, m = map(int, input().split())
# ls = []
# for i in range(n):
#     ls.append(list(map(int, input().split())))
# q = int(input())
# s = []
# for i in range(q):
#     s.append(list(map(int, input().split())))
#
# for i in range(len(ls)):
#     print(*ls[i])
#
# print(np.cross(ls, s))


# =================== 211 ======================

# a = map(int, input().split())
# ls, ls1 = list(map(int, input().split())), list(map(int, input().split()))
# print(*sorted(ls + ls1))

# =========================