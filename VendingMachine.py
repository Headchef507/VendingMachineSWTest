class VendingMachine:
    coininsert = False
    stock = 0
    def request_bottle(self):
        if(self.coininsert):
            return 1
        else:
            return 0
    def insert_coin(self):
        if(self.stock > 0):
            self.coininsert = True
        else:
           raise Exception("Stock is empty, please refill to continue") 
    def __init__(self, stock=0):
        self.stock = stock
        print('hello world')
p1 = VendingMachine()