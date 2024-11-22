# =================== 23 =====================
# from math import tan, sin, cos
#
# a, b, c, d, x = map(float, input().split())
# if a == 0:
#     print(f'{1.00:.2f}')
# else:
#     y2 = ((a * (x ** 2) + (b * x) + c) / (x * (a ** 3) + (a ** 2) + a ** (b - c))) + cos(abs(((a * x) + b) / ((c * x) + d + (2 ** c))))
#     print(f'{y2:.2f}')


# =================== 27 ======================
# from math import sqrt, tan, cos, sin
#
# x = float(input())
#
# aa = sqrt(((2 * tan(x + 2)) - cos(x + pow(2, x))) / (1 + pow(cos(x + 2), 2))) + (sin(pow(x, 2)) / (pow(x, 2) + 3))
# print(f'{aa:.2f}')


# =================== 35 ========================

# a, b, c = map(int, input().split())
# print(a * 2, b * 2, c * 2) if c <= b <= a else print(abs(a), abs(b), abs(c))

# ================= 36 ============================

# a, b = map(int, input().split())
# print(a) if a > b else print(a, b)

# =============== 37 =============================

# a, b = map(int, input().split())
# print(0 , b) if a <= b else print(a, b)

# ============== 38 ===============================

# x, y, z = map(float, input().split())
# lst = [x, y, z]
# for i in lst:
#     if 1 < i < 3:
#         print(i, end=' ')

# =============== 39 =========================

# x, y = map(int, input().split())
# print((x + y) / 2, float(2 * x * 2 * y)) if x < y else print(float(2 * x * 2 * y), (x + y) / 2)


# ================ 40 ========================

# x, y, z = map(int, input().split())
# lst = [x, y, z]
#
# for i in lst:
#     if i > 0:
#         print(pow(i, 2), end=' ')
#     else:
#         print(i, end=' ')


# ==================== 43 ======================

# x, y = map(float, input().split())
#
# if x < 0 and y < 0:
#     print(abs(x), abs(y))
# elif x < 0 or y < 0:
#     print(x + 0.5, y + 0.5)
# else:
#     print(x, y)


# ======================== 44 ======================

# x, y, z = map(int, input().split())
#
# if x + y > z and x + z > y and y + z > x:
#     print('YES')
# else:
#     print("NO")

# ======================== 45 =====================


