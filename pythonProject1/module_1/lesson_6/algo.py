# print(*[i for i in input().split()])

# print(input())

# ========================== cava 1 ============================
# _ , s = [st:=input()], [st[i] for i in range(len(st) - 1) if st[i] == st[i + 1]]
# print(*s)

# ========================== cava 2 =======================================

# print(*[i for i in input() if i.isupper()])

# print(' '.join([i for i in input() if i.isupper()]))

# ========================== cava 3 =======================================

# print(bool(True if [1 for i in input() if 65 < ord(i) < 90 or 97 < ord(i) < 122] else False))

# ====================== 165 ===========================
# from cmath import sin
#
# s, t = map(float, input().split())
#
#
# def f(a: float, b: float, c: float) -> float:
#     s = (2 * a - b - sin(c)) / (5 + abs(c))
#     a = f'{s:.2f}'
#     return a
#
#
# result = f(t, -2 * s, 1.17) + f(2.2, t, s - t)
# print(result)