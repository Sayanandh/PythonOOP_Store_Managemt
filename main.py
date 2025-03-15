class Item:
    pay_rate=0.8
    def __init__(self , name:str , price:float , quantity:int):
        assert price>=0 , f"Price no grater than 0"
        assert quantity>=0
        self.name = name
        self.price = price
        self.quantity = quantity
        ls=[]
        ls.append(self.name)
        print(ls)
    def calu_totalprice(self):
        return self.price * self.quantity
    
    def applydis(self):
        self.price=self.price * Item.pay_rate
        print(self.price)

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)
