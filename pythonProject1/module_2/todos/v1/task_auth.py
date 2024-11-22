from symtable import Class
from typing import Optional

users: list['User'] = []
todos: list = []

session_user: Optional['User'] = None


class User:
    def __init__(self,
                 id: int = None,
                 fullname: str = None,
                 username: str = None,
                 password: str = None
                 ) -> None:
        self.id = id
        self.fullname = fullname
        self.username = username
        self.password = password

    def is_validation(self) -> tuple[bool, str]:  # register
        for user in users:
            if user.username == self.username:
                return False, "Users have this Users"
        if len(self.password) < 4:
            return False, "Is valid password"
        return True, "Valid database"

    def save(self) -> None:
        self.id = users[-1].id + 1 if users else 1
        users.append(self)

    def login(self):
        for user in users:
            if user.username == self.username:
                if user.password == self.password:
                    return True, "Welcome your account"
                else:
                    return False, "Wrong password"
        return False, "Not found account"

    def __repr__(self):
        return f"{self.__class__.__name__}( id = {self.id}, fullname = {self.fullname}, username = {self.username}, password = {'*' * len(self.password)}"


class Setting:
    def setting(self):
        meny = input("""
        1) Edit account
        2) About
        3) Delete account
        0) Back
        >>>""")
        match meny:
            case "1":
                self.edit()
            case "2":
                self.about()
            case "3":
                self.delete()
            case "0":
                UI().account()

    def edit(self):
        meny = input("""
        1) Fullname
        2) Username
        3) Password
        0) Back
        >>>""")
        if meny == '0':
            self.setting()
        new_value = input("Enter new value: ")
        match meny:
            case '1':
                session_user.fullname = new_value
                self.setting()
            case '2':
                is_valid, message = User(username=new_value).is_validation()
                if is_valid:
                    session_user.fullname = new_value
                print(message)
                self.setting()
            case '3':
                is_valid, message = User(username=new_value).is_validation()
                if is_valid:
                    session_user.password = new_value
                print(message)
                self.setting()

    def about(self):
        print(session_user)
        self.setting()

    def delete(self):
        text = input('Do you want your account delete [N/y]: ')
        if text == 'y':
            users.remove(session_user)
        UI().main()


class Panel:
    def panel(self):
        pass


class UI:

    def register(self):
        user = {
            "fullname": input("Fullname : "),
            "username": input("Username : "),
            "password": input("Password : "),
        }
        user = User(**user)
        is_valid, message = user.is_validation()
        if is_valid:
            user.save()
        print(message)
        self.main()

    def login(self):
        global session_user
        user = {
            "username": input("Enter username: "),
            "password": input("Enter password: ")
        }
        is_valid, response = User(**user).login()
        if is_valid:
            session_user = response
            self.account()
            return
        print(response)
        self.main()

    def account(self):
        meny = input("""
        1) Panel
        2) Setting
        0) Logout
        >>> """)
        match meny:
            case "1":
                Panel().panel()
            case "2":
                Setting().setting()
            case "0":
                self.main()

    def main(self):
        menu = input("""
            1) Register
            2) Login
            3) Exit
            >>>""")
        match menu:
            case '1':
                self.register()
            case '2':
                self.login()
            case '3':
                return


UI().main()
