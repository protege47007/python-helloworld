

from sqlite3 import __connect


class Item:
    pay_rate = 0.8
    all = [] 


    def __init__(self, name: str, price: float, qty = 0): 
        # running validations of received args
        assert price >= 0, f"Price \"{price}\" is not greater than or equal to zero!" # assertion's second arg is an error message 
        assert qty >= 0, f"Quantity \"{qty}\" is not greater than or equal to zero!"
        
        # pass args to self obj
        
        self.__name = name # python sets this "__name" to be a private  property  
        self.__price = price
        self.qty = qty

        # actions to execute after instantiating
        Item.all.append(self)

    @property # this is a Getter method for the name property
    def name(self):
        return self.__name
    @property
    def price(self):
        return self.__price


    @name.setter # @name is identifier of the getter method initialized with the @property decorator 
    def name(self, val):
        # restriction/validation can be done here as it bypasses the constructor's assertion 
        if type(val) is str and len(val) < 10:
            self.__name = val
        else:
            raise Exception("value entered is either not a string or too long")

    def calculate_total_price(self):
        return self.__price * self.qty
    
    def apply_discount(self):
        return self.__price * self.pay_rate 

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.qty})"
    
    def __connect(self, smtp_server):
        pass

    def __prepare_body(self):
        return f"""
        Hello customer,

        we have your order of {self.__name}, Quantity: {self.qty}
        cost: {self.__price * self.qty + (self.__price * self.qty) * 0.2 }

        thanks for shopping with us
        """
    
    def __send(self): 
        # adding double underscore before the method's name 
        # abstracts this method from other classes and makes it private
        pass

    def send_email(self):
        self.__connect(200345)
        self.__prepare_body()
        self.__send()

        
