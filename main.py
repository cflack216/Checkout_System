class Inventory:
    shelf = []
    def __init__(self):
        self.shelf.append(Item(3.99, "bread", 1231))
        self.shelf.append(Item(2.99, "chocolate", 9999))
        self.shelf.append(Item(6.99, "charger", 7874))
        self.shelf.append(Item(9.99, "book", 9785))
        self.shelf.append(Item(19.99, "model", 2934))

    def search(self, UPC):
        for i in self.shelf:
            if i.UPC == UPC:
                return i
        return Item(999, "sentinel", 1234)


class Item:
    def __init__(self, price, name, upc):
        self.price = price
        self.description = name
        self.UPC = upc

    def scan(self):
        print(self.description + " $" + str(self.price))


x = Inventory()
total = 0.00

while True:
    try:
        UPC = int(input("Please Scan Item\n"))
    except:
        break
    item = x.search(UPC)
    item.scan()
    total += item.price

total += (.08 * total)
total = round(total,2)
print("total $" + str(total))
