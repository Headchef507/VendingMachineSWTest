class VendingMachine:
    def __init__(self, stock=0):
        self.check_value(stock)
        if stock < 0:
            raise ValueError("The class VendingMachine must be initialized with a positive value")
        if type(stock) != int:
            raise TypeError("The inputted value must be an integer or empty.")
        self.stock = stock

    def check_value(self, stock=0):
        if stock < 0:
            raise ValueError("The value for stock must be a positive value.")
        elif type(stock) != int:
            raise TypeError("The value for stock must be an integer.")
    
    def get_stock(self):
        return self.stock