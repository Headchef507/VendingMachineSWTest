class VendingMachine:
<<<<<<< HEAD
    max_stock = 0
    stock = 0
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
    
    def refill(self, stock):
        self.check_value(stock)
        self.check_value(self.stock + stock)
        self.stock = self.stock + stock
    
    def get_stock(self):
        return self.stock

class Bottle:
    milli_liter = 0
    def __init__(self):
        self.milli_liter = 500
=======
    coininsert = False
    stock = []
    def request_bottle(self):
        if(self.coininsert):
            self.coininsert = False
            bottle = self.stock.pop(0)
            return bottle
        else:
            raise Exception("Please insert a coin")
    def insert_coin(self):
        if(self.coininsert):
            raise Exception("Coin already inserted. Please request a bottle") 
        if(self.get_size_of_stock() > 0):
            self.coininsert = True
        else:
           raise Exception("Stock is empty, please refill to continue") 
    def get_size_of_stock(self):
        return len(self.stock)
    def __init__(self, stock=[]):
        self.stock = stock
class Bottle:
    milli_liter = 0
    def __init__(self):
        milli_liter = 500
>>>>>>> request-bottle-test-cases
