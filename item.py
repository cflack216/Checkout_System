class Item:

    def __init__(self, price, name, upc):
        self.price = price
        self.description = name
        self.UPC = upc

    def scan(self):
        print(self.description + " $" + str(self.price))