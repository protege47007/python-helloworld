import csv


class Item:
    pay_rate = 0.8
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

    @classmethod 
    def instantiate_from_csv(cls): 
        with open("items.csv", "r") as f:
            items = list(csv.DictReader(f))

            for item in items:
                Item(item.get("name"), price = float(item.get("price")), qty = int(item.get("qty")))
        
