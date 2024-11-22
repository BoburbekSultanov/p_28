class Person:
    def __init__(self,
                 name: str,
                 family: str,
                 age: int,
                 phone_number: str,
                 email: str,
                 adress: str,
                 id: str,
                 ):
        self.name = name
        self.family = family
        self.age = age
        self.phone_number = phone_number
        self.email = email
        self.adress = adress
        self.id = id

    def __repr__(self):
        pass
