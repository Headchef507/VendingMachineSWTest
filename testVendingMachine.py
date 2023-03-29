import unittest
import VendingMachine


class testVendingMachine(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")
    
    def test_request_bottle(self):
        vendingMachine = VendingMachine.VendingMachine()
        self.assertEqual(1,vendingMachine.request_bottle())
    
    def test_request_bottle_where_coinIsInserted(self):
        vendingMachine = VendingMachine.VendingMachine()
        vendingMachine.insert_coin()
        self.assertEqual(1,vendingMachine.request_bottle())

if __name__ == '__main__':
    unittest.main()