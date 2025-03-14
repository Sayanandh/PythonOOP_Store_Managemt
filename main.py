class Item:
    def __init__(self , name , price , quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calu_totalprice(self):
        return self.price * self.quantity


item1=Item("Phone" , 1000 , 5)
item2=Item("Laptop" , 10000 , 5)

print(item1.calu_totalprice())


