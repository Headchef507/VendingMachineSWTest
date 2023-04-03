
class Bottle:
    milli_liter = 0
    def __init__(self):
        self.milli_liter = 500


class VendingMachine:
    coininsert:bool = False
    capacity = 10
    stock:list[Bottle] = []

    # def __init__(self, new_stock:list[Bottle]=[]):
    def __init__(self, new_stock=[]):
        self.populate(new_stock)
    
    def populate(self, new_stock):
        if type(new_stock) != list:
            raise TypeError("Given argument must be of type list.")
        else:
            if (len(new_stock) + len(self.stock)) > self.capacity:
                raise IndexError("total amount of bottles may not exceed capacity.")
            for bottle in new_stock:
                if type(bottle) != Bottle:
                    raise TypeError("Each item in the given list must be of type bottle.")
                else:
                    self.stock.append(bottle)

    def request_bottle(self):
        if(self.coininsert):
            self.coininsert = False
            bottle = self.stock.remove(0)
            return bottle
        else:
            raise Exception("Please insert a coin")
        
    def insert_coin(self):
        if(self.coininsert):
            raise Exception("Coin already inserted. Please request a bottle") 
        if(self.get_size_of_stock() < 1):
            self.coininsert = True
        else:
           raise Exception("Stock is empty, please refill to continue") 
        
    def get_size_of_stock(self):
        return len(self.stock)
   
    def refill(self, stock):
        self.populate(stock)
