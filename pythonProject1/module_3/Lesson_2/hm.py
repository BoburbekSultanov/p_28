users = [
    {
        "id": 1,
        "username": "botir",
        "password": "1111",
        "role": "ADMIN"
    },
    {
        "id": 2,
        "username": "baxa",
        "password": "2222",
        "role": "USER"
    },
    {
        "id": 3,
        "username": "jamol",
        "password": "0000",
        "role": "USER"
    }
]

# def is_valid(temp):
#     def inner(function):
#         def wrapper(*args, **kwargs):
#             func = function(*args, **kwargs)
#             for user in users:
#                 if temp.lower() == user.get('role').lower() == 'admin':
#                     return user
#                 else:
#                     return "Not found account!"
#         return wrapper
#     return inner
#
#
# @is_valid('user')
# def to_print(*args, **kwargs):
#     return sum(args)
#
#
# print(to_print())


# def permission(role : list= []):
#     def inner(function):
#         def wrapper(*args , **kwargs):
#             for user in users:
#                 if user.get("username") == kwargs.get("username"):
#                     if user.get("password") == kwargs.get("password"):
#                         if user.get("role") in role:
#                             func = function(*args)
#                             return func
#                         else:
#                             return "Permission denied"
#                     else:
#                         return "Password not match"
#             return "Not Found account"
#         return wrapper
#     return inner


# ===================== Task 2 ================================


def with_file(st=False):
    def inner(function):
        def wrapper(*args, **kwargs):
            func = function(*args, **kwargs)
            if st:
                with open('text.txt', 'w') as f:
                    f.write(func)
            else:
                return func
        return wrapper
    return inner


@with_file()
def temp():
    return "Hello world"


# ====================== Task 3 ================================

# date = "2023-01-01 12:12:12"
# print(datetime.datetime.fromisoformat(date).timestamp())
#
# print(datetime.datetime.fromtimestamp(1672557132))
