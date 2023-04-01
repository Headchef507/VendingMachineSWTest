import unittest
import VendingMachine


class testVendingMachine(unittest.TestCase):

    def test_request_bottle_where_coinIsNotInserted(self):
        vendingMachine = VendingMachine.VendingMachine()
        self.assertEqual(0,vendingMachine.request_bottle())
    
    def test_request_bottle_where_coinIsInserted(self):
        vendingMachine = VendingMachine.VendingMachine()
        vendingMachine.insert_coin()
        self.assertEqual(1,vendingMachine.request_bottle())
    
    def test_insertCoin_stockIsEmpty(self):
        self.assertEqual(0,1)

if __name__ == '__main__':
    unittest.main()