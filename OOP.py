class Item:
    def calculate_total_price(self, price, qty): #this is called a method and not a function when it is attached to a class
        return price * qty

item1 = Item()
item1.name = "phone"
item1.price = 500
item1.qty = 2
print(f"{item1.name}: costs N{item1.calculate_total_price(item1.price, item1.qty)}")


class User:
    def __init__(self, name, age, phone_os) : #class initialization 
        self.name = name
        self.age = age
        self.phone_os = phone_os

josh = User("Josh", 26, "Android")

print(josh.name, josh.age, josh.phone_os)


class Item2:
    def __init__(self, name: str, price: float, qty = 0):
        # running validations of received args
        assert price >= 0, f"Price \"{price}\" is not greater than or equal to zero!" # assertion's second arg is an error message 
        assert qty >= 0, f"Quantity \"{qty}\" is not greater than or equal to zero!"
        
        # pass args to self obj
        self.name = name
        self.price = price
        self.qty = qty

    def calculate_total_price(self):
        return self.price * self.qty

item3 = Item2("phone", 500, 2)
item3.has_numpad = False

print(f"{item3.name}: costs N{item3.calculate_total_price()}")