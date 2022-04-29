class Item:
    all = [] 


    def __init__(self, name: str, price: float, qty = 0): 
        # running validations of received args
        assert price >= 0, f"Price \"{price}\" is not greater than or equal to zero!" # assertion's second arg is an error message 
        assert qty >= 0, f"Quantity \"{qty}\" is not greater than or equal to zero!"
        
        # pass args to self obj
        self.name = name
        self.price = price
        self.qty = qty

        # actions to execute after instantiating
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.qty
    
    def apply_discount(self):
        return self.price * self.pay_rate 

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.qty})"

class Phone(Item):

    def __init__(self, name: str, price: float, qty = 0, broken_qty = 0):
        super().__init__(name, price, qty)

        # validation
        assert broken_qty >= 0, f"Quantity of broken phones should be greater than or equal to 0: \"{qty}\""

        # initialization of instance
        self.broken_qty = broken_qty


phone1 = Phone("Redmi", 1000, 16, 2)

print(phone1.calculate_total_price())
print(Item.all)
print(Phone.all) # the all attribute is served by the super/parent class