class VendingMachine:
    coininsert = False
    stock = 0
    def request_bottle(self):
        if(self.coininsert):
            self.coininsert = False
            self.stock -= 1
            return 1
        else:
            raise Exception("Please insert a coin")
    def insert_coin(self):
        if(self.coininsert):
            raise Exception("Coin already inserted. Please request a bottle") 
        if(self.stock > 0):
            self.coininsert = True
        else:
           raise Exception("Stock is empty, please refill to continue") 
    def __init__(self, stock=[]):
        self.stock = stock
class Bottle:
    milli_liter = 0
    def __init__(self):
        milli_liter = 500