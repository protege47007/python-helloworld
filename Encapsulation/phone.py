from item import Item

class Phone(Item):

    def __init__(self, name: str, price: float, qty = 0, broken_qty = 0):
        super().__init__(name, price, qty)

        # validation
        assert broken_qty >= 0, f"Quantity of broken phones should be greater than or equal to 0: \"{qty}\""

        # initialization of instance
        self.broken_qty = broken_qty
