class VendingMachine:
    def __init__(self, stock=0):
        self.max_stock = 10
        self.check_value(stock)
        self.stock = stock

    def check_value(self, stock=0):
        if stock < 0:
            raise ValueError("The value for stock must be a positive value.")
        elif type(stock) != int:
            raise TypeError("The value for stock must be an integer.")
        elif stock > self.max_stock:
            raise ValueError("The value for stock must not be greater than the maximum stock.")
    
    def get_stock(self):
        return self.stock