import item
class Inventory:

    shelf = []
    def __init__(self):
        self.shelf.append(item.Item(3.99, "bread", 1231))
        self.shelf.append(item.Item(2.99, "chocolate", 9999))
        self.shelf.append(item.Item(6.99, "charger", 7874))
        self.shelf.append(item.Item(9.99, "book", 9785))
        self.shelf.append(item.Item(19.99, "model", 2934))

    def search(self,UPC):
        for i in self.shelf:
            if i.UPC == UPC:
                return i
            else:
                return item.Item(999, "sentinel", 1234)
