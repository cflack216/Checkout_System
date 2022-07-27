import inventory

x = inventory.Inventory()
total = 0

while True:
    try:
        UPC = int(input("Please Scan Item\n"))
    except:
        break
    item = x.search(UPC)
    item.scan()
    total+=item.price

total+=(.08*total)
print("total $" + str(total))