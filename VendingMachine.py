class VendingMachine:
    coininsert = False
    def request_bottle(self):
        if(self.coininsert):
            return 1
        else:
            return 0
    def __init__(self):
        #self.inventory = inventory
        print('hello world')
p1 = VendingMachine()