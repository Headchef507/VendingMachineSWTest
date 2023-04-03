class VendingMachine:
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