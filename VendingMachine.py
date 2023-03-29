class VendingMachine:
    def __init__(self, stock=0):
        self.stock = stock
    
    def get_stock(self):
        return self.stock