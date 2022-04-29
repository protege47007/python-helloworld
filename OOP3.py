# difference between a static method and a class method

# the first arg/param passed in a class method is the class obj itself, while in
# a static method, the class or self (instance of the class) obj is not passed

# a class method has direct relationship with the class it is been called from, while 
# a static method is just basically an ordinary function that doesn't uniquely has a
# relationship with the class obj


class Item:
    @classmethod
    def instantiate_from_csv(cls):
        pass

    @staticmethod
    def is_integer(num):
        pass