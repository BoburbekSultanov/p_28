# ========================= task 1 ========================================
# my_dict = {
#     'b123o234o23k': '',
#     'la234p32t324op': ''
# }
# st = list(my_dict.keys())
# my_dict.clear()
# for i in st:
#     keys, values = ''.join(list(filter(lambda char: char.isalpha(), i))), ''.join(list(filter(lambda char: not char.isalpha(), i)))
#     my_dict[keys] = values
# print(my_dict)
import pprint

# =========================== task 2 =======================================

# math = 'Loren inpus Is simply dummy text of the printing'
# d = {}
# for i in sorted(list(set(math.replace(' ', '')))):
#     d[i] = math.count(i)

# for i in sorted(math.replace(' ', '')):
#     d[i] = d.get(i, 0) + 1

# print(d)


# ========================= task 3 =========================================


products = []
# s = True
# while s:
#     firma_dict = {}
#     firma_dict["product_name"] = input('Mahsulot nomini kiriting: ')
#     firma_dict["product_count"] = int(input('Mahsulot sonini kiriting: '))
#     firma_dict["product_price"] = int(input('Mahsulot narxini kiriting: '))
#     products.append(firma_dict)
#     if input("Yana xoxlasayiz 'YES' tugatish uchun 'NO' ").upper() == 'NO':
#         s = False
#
# print(products)

# while True:
#     menu = """
#         1) Product add
#         2) Product list
#         3) Product exit
#     >>>>> """
#     key = int(input(menu))
#     if key == 1:
#         name = input('New Product name: ')
#         price = input('New Product price: ')
#         name = input('New Product name: ')
