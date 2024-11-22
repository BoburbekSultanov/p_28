customers = []


class Customers:
    def __init__(self, name: str, company: str, email: str, password: str):
        self.name = name
        self.company = company
        self.email = email
        self.password = password

    def is_valid(self):
        if not '@' in self.email:
            return False, 'Invalid email'
        if len(self.password) < 4:
            return False, 'Invalid password'
        return True, "Date valid"

    def about_customer(self):
        text = f"""
        name customer : {self.name}
        company : {self.company}
        email : {self.email}
        password : {self.password}
        """
        return text

    def change_name(self, new_name):
        self.name = new_name

    def sing_up(self):

        is_valid, message = self.is_valid()
        if not is_valid:
            return message
        else:
            customers.append(self)


while True:
    customer_name = input('Enter your name: ')
    customer_company = input('Enter your company: ')
    customer_email = input('Enter your email: ')
    customer_password = input('Enter your password: ')
    costomer = Customers(customer_name, customer_company, customer_email, customer_password)
    print(costomer.about_customer())
