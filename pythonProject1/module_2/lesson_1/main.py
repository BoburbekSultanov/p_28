# class Shape:
#     pass
#
#
# class Animal:
#     pass
# import datetime
#
#
# class User:
#     new_year = datetime.datetime.now().year
#
#     def __init__(self, name, age, email, phone_number):
#         self.name = name
#         self.age = age
#         self.email = email
#         self.phone_number = phone_number
#
#     def about_user(self):
#         text = f"""
#         user name : {self.name}
#         user age : {self.age}
#         user email : {self.email}
#         user phone number : {self.phone_number}
#         """
#         print(text)
#
#     def get_brith_year(self):
#         return self.new_year - self.age
#
#
# user1 = User(name='Boburbek', age=29, email='sultanov@gmail', phone_number=9998909279998)
# user1.about_user()
# print(user1.get_brith_year())


# print(user1.name, user1.age, user1.email, user1.phone_number)
# user1.phone_number(9090)
# print(user1.name, user1.age, user1.email, user1.phone_number)


# ======================== Task 1 =============================

# class Shape:
#     def __init__(self, name, radius):
#         self.name = name
#         self.radius = radius
#
#
# class Animal:
#     def __init__(self, name, place_residence):
#         self.name = name
#         self.place_residence = place_residence
#
#
# circle = Shape(name='circle', radius=23)
# monkey = Animal(name='monkey', place_residence='Forset')
# print(monkey.name, monkey.place_residence, sep='\n')


