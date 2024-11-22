def increase(ls: list) -> float:
    s = 1
    for i in ls:
        if isinstance(i, int):
            s *= i
    return s


# ===================== 101 ========================

# input()
# lst = list(map(int, input().split()))
# ls = [i for i in lst if sum(lst) / len(lst) > i]
# print(f'{sum(ls) / len(ls):.2f}')


# =================== 102 =========================

# input()
# ls = list(map(int, input().split()))
# ab = list(map(int, input().split()))
# lst = [(round(i / min(ls) + 0.01, 1) if min(ls) <= i else float(i)) for i in ls[ab[0] - 1: ab[1]]]
# lst1 = ls[:ab[0] - 1] + lst + ls[ab[1]:]
# lst1 = [float(i) for i in lst1]
# print(*lst1)

# ======================== 103 ====================================


# n, ls = input(), list(map(int, input().split()))
# k, i = map(int, input().split())
# print(f'{sum(ls[k - 1:i]) / len(ls[k - 1: i]):.1f}')

# =========================== 105 ================================
# def algo105(ls: list, k: int, i: int) -> float:
#     ls = ls[:k - 1] + ls[i:]
#     s = f'{sum(ls) / len(ls):.2f}'
#     return s


# n, ls = input(), list(map(int, input().split()))
# k, i = map(int, input().split())
# print(algo105(ls, k, i))
# ls = ls[:k - 1] + ls[i:]
# print(ls)

# ========================== 106 ===============================

# n, ls = int(input()), list(map(int, input().split()))
# print(sum([i ** 2 for i in ls ]))

# ======================== 107 ================================

# n, ls = int(input()), list(map(int, input().split()))
# print(*[f'{(i / max(ls)):.2f}' for i in ls ])

# ====================== 108 =================================

# n, ls = int(input()), list(map(int, input().split()))
# print(*[f'{(i / min(ls)):.2f}' for i in ls ])

# ===================== 109 ================================
# from math import log
# n, ls, m = int(input()), list(map(int, input().split())), int(input())
# res = 1
# for i in ls:
#     if m < i:
#         res *= i
# print(f'{log(res):.2f}')

# ===================== 110 ===========================

# n, ls = int(input()), list(map(int, input().split()))
# k, m = map(int, input().split())
# res = 1
# for i in ls:
#     if i == k or i == m:
#         res *= i
# print(res)


# =========================== 111 ========================

# n, ls, m = input(), list(map(int, input().split())), int(input())
# print(sum([i for i in ls if i > m]))

# ========================= 112 =========================

# m, ls = int(input()), list(map(int, input().split()))
# s = 0
# k = 1
# for i in range(m):
#     if not i % 2:
#         k *= ls[i]
#     else:
#         s += ls[i]
# print(f'{k/s:.2f}')

# ======================== 113 =========================

# m, ls = input(), list(map(int, input().split()))
# print(f'{(sum([i for i in ls if i < 0])) / len([i for i in ls if i < 0]):.2f}')

# ===================== 114 =============================
# from math import sin
#
# n, ls = input(), list(map(int, input().split()))
# print(f'{sin(increase([i for i in ls if not i % 2 or not i % 5])):.2f}')

# ====================== 115 ===========================

# n, ls, m = input(), list(map(int, input().split())), int(input())
# print(f'{sum([i ** 2 for i in ls if m > i])}')

# ======================= 116 ==========================

# n , ls = input(), list(map(int, input().split()))
# print(*[f'{i / max(ls) + 0.000001:.2f}' for i in ls])

# ======================== 117 ========================

# n , ls = input(), list(map(int, input().split()))
# print(sum([ls[i] for i in range(0, len(ls), 2)]))

# ===================== 118 ============================

# n, ls = int(input()), list(map(int, input().split()))
# print(f'{sum([i for i in ls if i % 2]) / len([i for i in ls if i % 2]) + 0.000001:.2f}')

# ====================== 120 ===========================

# n, ls = input(), list(map(int, input().split()))
# x, y = map(int, input().split())
# print(len([i for i in ls if x > i or i > y]))

# ===================== 121 ============================

# n, ls, m = input(), list(map(int, input().split())), int(input())
# print(sum(ls[m:]))

# ===================== 122 ============================

# n, ls = input(), list(map(int, input().split()))
# print(sum([i ** 2 for i in ls]), f'{sum(ls)/ len(ls):.2f}', sep='\n')

# ==================== 123 =============================

# n, ls = int(input()), list(map(int, input().split()))
# s = sum([ls[i] for i in range(1, n, 2)])
# print(*[f'{i / s + 0.00001:.2f}' if i > 0 and i % 2 else f'{i:.2f}' for i in ls])

# ====================== 124 =============================
# s = {'4', '6', 79, 80, 100, '1', '2'}
# print({['1', '2', 4]}.isdisjoint(s))


d = {1:'1', 2:'2'}
print(d.get(4, 'salom'))