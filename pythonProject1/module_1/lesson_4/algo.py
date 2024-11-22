# =============== 165 ====================
# from math import sin
#
# s, t = map(float, input().split())
#
#
# def f(a: float, b: float, c: float) -> float:
#     result = ((2 * a) - b - (sin(c))) / (5 + abs(c))
#     a = round(result, 2)
#     return a
#
#
# print(f'{f(t, (- 2 * s), 1.17):.2f}')
# print(f'{f(2.2, t, s - t):.2f}')
# print(f'{f(t, (- 2 * s), 1.17) + f(2.2, t, s - t):.2f}')


# ==================== 147 ===========================

# def count_a_y(st: str) -> int:
#     return st.count('A')
#
#
# print(count_a_y(input('matn kiriting: ')))

# ================= 148 ==============================


# print(*[i for i in input().split() if i[0] == 'A'], sep='\n')


# ==================== 149 ============================


# result = [i for i in input().split() if i[-2:] == 'NA']
# print(len(result))
# print(*result)

# ===================== 150 ===========================


# print(*[i for i in input().split() if 'info' in i.lower()])

# ==================== 151 ============================


# c = [i for i in input().lower() if i in 'aoiue']
# print(len(c))


# ====================== 152 ==========================

# print(input()[::-1])

# ====================== 153 ==========================

# for i in input().split():
#     print(i, len(i))


# ====================== 154 ==========================


# print(sum([int(i) for i in input() if i.isdigit()]))


# =================== 155 =============================

# print(sum([1 for i in input().split() if i[0].isupper()]))


# ======================= 156 ============================

# st = input().split()
# i, j = map(int, input().split())
# st[i - 1], st[j - 1] = st[j - 1], st[i - 1]
# print(*st)


# ======================= 157 ============================

# st = input().split()
# i = int(input())
# st[i - 1] = 'TATU'
# print(*st)


# ===================== 158 =============================


# odd = 0
# couple = 0
# for i in input().split():
#     if len(i) % 2:
#         odd += 1
#     else:
#         couple += 1
# print(odd * couple)


# ====================== 159 ============================

# print(sum([1 for i in input().split() if i[0] == 'a' and i[-1] == 'b']))

# ============================= 160 ======================


# print(input().swapcase())

# =========================== 161 =============================
# n = input()
# st = input()
# print('YES' if st.count('A') >= 2 and st.count('S') >= 2  and st.count('L') >= 1 and st.count('O') >= 1 and st.count('M') >= 1 else 'NO')


# =========================== 162 =============================

# n = input()
# print(input().replace('$', ''))

# ========================== 163 ===============================

# num = ''
# for i in input().split():
#     if len(i) > len(num):
#         num = i
# print(num)

# ========================= 164 ==================================

# st = input()
# l, r = map(int, input().split())
#
# print(st[l - 1:r] if r > l else st[r - 1:l][::-1])

# strs = ["dog", "racecar", "car"]
# roman_dict = {
#     'I': 1,
#     'V': 5,
#     'X': 10,
#     'L': 50,
#     'C': 100,
#     'D': 500,
#     'M': 1000
# }



