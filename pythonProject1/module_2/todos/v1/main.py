"""TODO project"""
import email
from operator import rshift, index
from stringprep import c6_set
from typing import Optional

from pyexpat.errors import messages

users: list['User'] = []
todos = []
categories: list['Category'] = []
"""
Create
Read
Update
Delete
"""


class UserError(Exception):
    pass


# Back end
class CRUD:
    def save(self):
        pass

    def delete(self):
        pass

    def update(self, field, new_value):
        pass

    def get(self):
        pass


class User(CRUD):
    def __init__(self,
                 _id: int = None,
                 fullname: str = None,
                 email: str = None,
                 password: str = None) -> None:
        self.id = _id
        self.fullname = fullname
        self.email = email
        self.password = password

    def delete(self) -> None:
        for user in users:
            if user.id == self.id:
                users.remove(self)

    def update(self, field, new_value) -> None:
        for user in users:
            if user.id == self.id:
                setattr(user, field, new_value)

    def get(self) -> 'User':
        for user in users:
            if user.id == self.id:
                return user

    def about(self) -> str:
        text = f"""
        Fullname : {self.fullname}
        Email : {self.email}
        Password : {"*" * 8}
        """
        return text

    def is_validation(self) -> None:
        for user in users:
            if self.email and user.email == self.email:
                raise Exception("Already email")
        if self.password and len(self.password) < 4:
            raise Exception("Invalid pasword")
        if self.email and "@" not in self.email:
            raise Exception("'@' not in email")

    def save(self) -> None:
        self.id = users[-1].id + 1 if users else 1
        users.append(self)

    def login(self) -> 'User':
        for user in users:
            if user.email == self.email:
                if user.password == self.password:
                    return user
                raise Exception('Wrong password')
        raise Exception('Not found account')

    def __repr__(self):
        return f"User(id={self.id}, fullname={self.fullname},email={self.email},password={self.password})"


class Category(CRUD):

    def __init__(self, _id=None, name=None):
        self.id = _id
        self.name = name

    def search(self, short_name) -> None:
        result = []
        for category in categories:
            if category.name.lower().statrwith(short_name):
                result.append(self)

    def about(self) -> str:
        text = f"""
        Category ID : {self.id}
        Category name : {self.name}
        """
        return text

    def save(self) -> None:
        self.id = categories[-1].id + 1 if categories else 1
        categories.append(self)

    def delete(self) -> None:
        for category in categories:
            if category.id == self.id:
                categories.remove(self)

    def update(self, field, new_value) -> None:
        for category in categories:
            if category.id == self.id:
                setattr(category, field, new_value)

    def get_list(self):
        return categories

    def get(self) -> "Category":
        for category in categories:
            if category.id == self.id:
                return category

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} id = {self.id}, name = {self.name}"


class ToDo(CRUD):
    def __init__(self):
        pass


session_user: Optional['User'] = None


# Front end
class UICategory:
    session_category: Optional['Category'] = None

    def main(self):
        try:
            menu = """
                *) Search 🔍
                1) Add
                2) List
                0) <-back
                >>>"""
            key = input(menu)
            assert key in ("*", "1", "2", "0"), "Menuyada yo'q bo'lim tanlandi"

            match key:
                case "*":
                    short_name = input("🔍>>>")
                    pass

                case "1":
                    _name = input("Name:")
                    category = Category(name=_name)
                    category.save()
                    self.main()

                case "2":
                    for pos, category in enumerate(categories, 1):
                        print(f"{pos}) {category}")
                    menu = input("Enter possion")
                    self.main()
                case "0":
                    UIAccount().panel()
                    self.main()
        except AssertionError as message:
            print(message)
            self.main()

    def settings(self):
        try:
            menu = input("""
                        1) delete
                        2) update
                        3) about
                        0) <-back
                        >>>""")
            assert menu not in ('1', '2', '3', '0'), "Menuyada yo'q bo'lim tanlandi"
            match menu:
                case "1":
                    pass
                case "2":
                    pass
                case "3":
                    pass
                case "0":
                    pass
        except AssertionError as massage:
            print(massage)
            self.settings()


class UIAccount:
    def panel(self):
        menu = """
            1) Category
            2) ToDo
            0) <-back
            >>>"""
        key = input(menu)
        match key:
            case "1":
                UICategory().main()
            case "2":
                pass
            case "0":
                self.account()

    def account(self):
        print(f"Welcome to account {session_user.fullname}")
        menu = """
           1) Panel
           2) settings
           0) logout
           >>>"""
        key = input(menu)
        match key:
            case '1':
                self.panel()
            case '2':
                self.settings()
            case '0':
                UI().main()

    def edit(self):
        try:
            fields = """
                1) fullname
                2) email
                3) password
                0) <-back
                >>>"""
            key = input(fields)
            if fields == '0':
                self.settings()
            new_value = input('Enter new value: ')
            match key:
                case '1':
                    session_user.fullname = new_value
                case '2':
                    user = User(email=new_value)
                    user.is_validation()
                    session_user.email = new_value
                case '3':
                    user = User(password=new_value)
                    user.is_validation()
                    session_user.password = new_value
            self.settings()
        except Exception as message:
            print(message)
            self.settings()

    def settings(self):
        menu = """
                1) Edit account
                2) About
                3) delete account
                0) <-back
                >>>"""
        key = input(menu)
        match key:
            case '1':
                self.edit()
            case '2':
                print(session_user.about())
                self.account()
            case '3':
                session_user.delete()
                UI().main()
            case '0':
                self.account()


class UI:

    def register(self):
        user = {
            "fullname": input("Enter your fullname:"),
            "email": input("Enter your email:"),
            "password": input("Enter your password:")
        }
        user = User(**user)
        user.is_validation()
        user.save()
        self.main()

    def login(self):
        global session_user
        login_data = {
            "email": input("Email:"),
            "password": input("Password:")
        }
        user = User(**login_data)
        session_user = user.login()
        UIAccount().account()

    def main(self):
        try:
            menu = """
                1) Register
                2) Login
                3) exit
                >>>"""

            key = input(menu)
            match key:
                case "1":
                    self.register()
                case "2":
                    self.login()
                case "3":
                    return
        except Exception as message:
            print(message)
            self.main()


UI().main()
