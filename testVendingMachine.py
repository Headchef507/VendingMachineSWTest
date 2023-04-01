import unittest
import VendingMachine


class testVendingMachine(unittest.TestCase):

    def test_request_bottle_where_coinIsNotInserted(self):
        vendingMachine = VendingMachine.VendingMachine()
        self.assertEqual(0,vendingMachine.request_bottle())
    
    def test_request_bottle_where_coinIsInserted(self):
        vendingMachine = VendingMachine.VendingMachine(1)
        vendingMachine.insert_coin()
        self.assertEqual(1,vendingMachine.request_bottle())
    
    def test_insertCoin_stockIsEmpty_exception(self):
        vendingMachine = VendingMachine.VendingMachine()
        with self.assertRaises(Exception):
            vendingMachine.insert_coin()

if __name__ == '__main__':
    unittest.main()