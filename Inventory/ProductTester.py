class Product:
    # constructor
    def __init__(self, item_num=0, name="null", quantity=0, price=0.0):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.item_num = item_num

    # accessors and mutators
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity

    def get_item_num(self):
        return self.item_num

    def set_item_num(self, item_num):
        self.item_num = item_num

    # returns string of inventory
    def str(self):
        return "itemNumber : " + str(self.item_num) + "\nName : " + self.name + "\nQuantity in stock : " \
               + str(self.quantity) + "\nPrice : " + str(self.price) + "\n"


# products created with default constructors
item1 = Product()
item2 = Product()

# products created with overloaded constructors
item3 = Product(3, "marker", 200, 7.75)
item4 = Product(4, "Colored Pencil", 500, 9.5)
item5 = Product(5, "Eraser", 150, 4.0)
item6 = Product(6, "Notebook", 400, 6.75)

# displaying inventory
print(item1.str())
print(item2.str())
print(item3.str())
print(item4.str())
print(item5.str())
print(item6.str())

# Sample Run
'''
itemNumber : 0
Name : null
Quantity in stock : 0
Price : 0.0

itemNumber : 0
Name : null
Quantity in stock : 0
Price : 0.0

itemNumber : 3
Name : marker
Quantity in stock : 200
Price : 7.75

itemNumber : 4
Name : Colored Pencil
Quantity in stock : 500
Price : 9.5

itemNumber : 5
Name : Eraser
Quantity in stock : 150
Price : 4.0

itemNumber : 6
Name : Notebook
Quantity in stock : 400
Price : 6.75

'''