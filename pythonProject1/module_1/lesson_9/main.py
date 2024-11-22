from pprint import pprint

users = [
    {
        "first_name": "Botirjon",
        "last_name": "Qodirov",
        "age": 17,
        "address": "Toshkent",
        "balance": 100_000
    },
    {
        "first_name": "Kamol",
        "last_name": "Doniyorov",
        "age": 17,
        "address": "Sirdaryo",
        "balance": 100_000_000
    },
]

# for user in users:
#     print(user.get("first_name"), user.get('last_name'))
#     print(user.get('age'))

# print(sum([i['balance'] for i in users]))

# s = input().lower()
# for i in users:
#     if s.lower() in i.get('first_name').lower() or s.lower() in i.get('last_name').lower():
#         pprint(i)


myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

s = 'Massiv List Set'
my_dict = {}
for i in s:
    if i.isalpha():
        my_dict.setdefault(i, s.count(i))
    # my_dict[i] = s.count(i)
for i in my_dict:
    print(i, my_dict[i])
