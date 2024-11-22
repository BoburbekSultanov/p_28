products: list['Product'] = []


class Product:

    def __init__(self, product_name: str,
                 product_price: float,
                 product_image: str
                 ):
        self.product_name = product_name
        self.product_price = product_price
        self.product_image = product_image

    def sing_up(self):
        products.append(self)

    def about_products(self):
        text = f"""
        Product name : {self.product_name.capitalize()}
        Product price : {self.product_price}
        Product image : {self.product_image}
        
        """
        return text

    def creat_product(self, name, price, image):
        self.product_name = name
        self.product_price = price
        self.product_image = image

    def product_note(self):
        return f'no such information'.capitalize()

    def change_product(self):
        text = input("""
                    1) Product name
                    2) Product price
                    3) Product image
                    >>> """)
        d = {
            "1": "name",
            "2": "name",
            "3": "name",
        }
        old_value = input('Enter old value: ')
        new_value = input('Enter new value: ')

        for item in products:
            if item.product_name.lower() == old_value.lower():
                setattr(item, d.get(text), new_value)
                setattr(item, d.get(text), new_value)
                setattr(item, d.get(text), new_value)
                break
        else:
            print(item.product_note())


while True:

    key = input("""
    1) create
    2) about
    3) change
    4) search
    5) delete
    >>> """)
    match key:
        case '1':
            product_name = input('Enter product name : ')
            product_price = float(input('Enter product price : '))
            product_image = input('Enter product image : ')
            obj = Product(product_name, product_price, product_image)
            obj.sing_up()

        case '2':
            for product in products:
                print(product.about_products())
        case '3':
            obj.change_product()

        case '4':
            pass
        case '5':
            pass
