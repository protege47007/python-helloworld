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
        return f"Item('{self.name}', {self.price}, {self.qty})"

    @classmethod # "cls" the class is passed instead of "self" which is an instance of the class object
    def instantiate_from_csv(cls): # this method is attached to the class Item and not the instance of the class
        with open("items.csv", "r") as f:
            # "csv" is imported above to open csv files
            # "DictReader(file)" converts the file into a dictionary (objects)
            # "list" combines the dictionaries into a list (array) 
            items = list(csv.DictReader(f))

            for item in items:
                Item(item.get("name"), price = float(item.get("price")), qty = int(item.get("qty")))
        
    @staticmethod
    # this is a static method (ordinary function) to determine if the arg "num" is an integer
    def is_integer(num):
        # isinstance checks if the arg "num" is instance of the class "float"
        # another example can be isinstance(5, bool) to check if 5 is an instance of class bool (Boolean)
        if isinstance(num, float):
            return num.is_integer() # is_interger is used to determine if the float is an integer e.g. 10.0
        # here isinstance checks if the arg "num" is an integer since it didnt pass as a float
        elif isinstance(num, int):
            # as the "is_integer()" function in the float block, a truthy value is returned
            # to denote that "num" is an integer
            return True
        else:
            # if "num" reaches here then it is neither a float or an integer
            return False


# Item.instantiate_from_csv() 

# print(Item.all)

# for instance in Item.all:
#     print(instance.name)

num = 5.0
print(Item.is_integer(num))
