class VendingMachine:
    def __init__(self, stock=0):
        if stock < 0:
            raise ValueError("The class VendingMachine must be initialized with a positive value")
        self.stock = stock
    
    def get_stock(self):
        return self.stock