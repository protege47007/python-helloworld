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
    pay_rate = 0.8 # this is a class attribute
    all = [] # a list of all instances created with this class


    def __init__(self, name: str, price: float, qty = 0): # this are instance attributes
        # running validations of received args
        assert price >= 0, f"Price \"{price}\" is not greater than or equal to zero!" # assertion's second arg is an error message 
        assert qty >= 0, f"Quantity \"{qty}\" is not greater than or equal to zero!"
        
        # pass args to self obj
        self.name = name
        self.price = price
        self.qty = qty

        # actions to execute after instantiating
        Item2.all.append(self)

    def calculate_total_price(self):
        return self.price * self.qty
    
    def apply_discount(self):
        return self.price * self.pay_rate # class attrs are not available at the instance level 

    def __repr__(self) -> str:
        return f"Item('{self.name}', {self.price}, {self.qty})" # this method prints to the all list

item3 = Item2("phone", 500, 2)
item3.has_numpad = False

item4 = Item2("laptop", 1000, 5)
item5 = Item2("mouse", 250, 5)
item6 = Item2("keyboard", 400, 3)
item7 = Item2("speakers", 600, 7)

print(f"{item3.name}: costs N{item3.calculate_total_price()}")
print(f"{item3.name}: costs at a discount is N{item3.apply_discount()}")
item3.pay_rate = 0.7
print(f"{item3.name}: costs at new discount is N{item3.apply_discount()}")

print(Item2.all)

for instance in Item2.all:
    print(instance.name)