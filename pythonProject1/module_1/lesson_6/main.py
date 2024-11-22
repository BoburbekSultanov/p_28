# 1.  n butun soni berilgan. Quyidagi yig’indini hisoblovchi dastur tuzilsin.
# S = 1 + 1/2 + 1/3 + …1/n.
# 2.  Foydalanuvchi tomonidan ikkita a va b sonlari kirtiladi. Kirtilgan sonlarning
#     EKUK(a, b) ni xisoblovchi dastur tuzilsin.
# 3.  N ta butun sonli 1 o’lchamli massiv berilgan. Shu massiveda nechta 3 xonali, nechta 2 xonali, nechta 1 xonali son bor ekanligini aniqlovchi dastur tuzing.
# 4.  N x M o’lchamdagi butun sonli massiv berilgan. Har bir ustunidagi elementlarning yig’indisini aniqlang.
# 5.  Str satr berilgan. Shu satrdagi barcha raqamlarni o’chirib qaytaruvchi agar raqam bo’lmasa satrni o’zini qaytaruvch funksiya tuzing
# 6.  Uzunligi kamida 2ga teng bo’lgan satr berilgan. Shu satrni oxirgi 2ta harfini 3 marta yonma-yon qilib natijani qaytaradigan funksiya tuzing.


# S = 1/1 + 1/2 + 1/3 + …1/n.

# 5
# s = 0
# for i in range(1, int(input()) + 1):  #  1 2 3 4 5
#    s += (1 / i)
# print(f'{s:.5f}')

# print(f'{sum([1 /i  for i in range(1, int(input()) + 1)]):.2f}')

# num1, num2 = map(int, input().split())
# ekuk = []
# for i in range(1, min(num1, num2) + 1):
#     if not num1 % i and not num2 % i:
#         ekuk.append(i)
# print(max(ekuk))

# print(max([i for i in range(1, min(num1, num2) + 1) if (not num1 % i and not num2 % i)]))

# n = [21, 345, 1, 21, 345, 1, 21, 345, 1, 21, 345, 1, 21, 345, 1, 21, 345, 1, 21, 345, 1, 345, 343, 32]
# n1, n2, n3 = 0, 0, 0
# for i in n:
#     if 0 < i < 9:
#         n1 += 1
#     if 9 < i < 100:
#         n2 += 1
#     if 99 < i < 1000:
#         n3 += 1
# print(n1, n2, n3)

# st = []
# for i in range(5):
#     st.append([1, 2, 3, 4, 5])
# # print(*st, sep='\n')
# for i in st:
#     sr = 0
#     for j in i:
#         if i == j and i > j:
#             sr += st[i][j]
#     print(sr)

# st = 'sfsd23324sdfsdf'
# temp = ''
# for i in st:
#     if i.isalpha():
#         temp += i
# print(temp)

# print(input()[-2:] * 3)

