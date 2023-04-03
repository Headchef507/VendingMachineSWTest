import unittest
import VendingMachine


class testVendingMachine(unittest.TestCase):
    def setUp(self) -> None:
        self.vm = VendingMachine.VendingMachine(5)
        bottle1 = VendingMachine.Bottle()
        bottle2 = VendingMachine.Bottle()

    # def test_sum(self):
        # self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")
    
    def test_empty_stock_is_zero(self):
        empty_vm = VendingMachine.VendingMachine()
        self.assertEqual(empty_vm.get_stock(), 0, "Should be 0")
    
    def test_5_stock_is_5(self):
        five_vm = VendingMachine.VendingMachine(5)
        self.assertEqual(five_vm.get_stock(), 5, "Should be 5")
    
    def test_negative_init(self):
        self.assertRaises(ValueError, VendingMachine.VendingMachine, -1)

    def test_non_int_init(self):
        self.assertRaises(TypeError, VendingMachine.VendingMachine, "3")
    
    def test_max_init(self):
        self.assertRaises(ValueError, VendingMachine.VendingMachine, 11)

    def test_refill5(self):
        # vm = VendingMachine.VendingMachine(5)
        self.vm.refill(5)
        self.assertEqual(self.vm.get_stock(), 10, "Should be 10")

    def test_refill3(self):
        # vm = VendingMachine.VendingMachine(5)
        self.vm.refill(3)
        self.assertEqual(self.vm.get_stock(), 8, "Should be 8")
    
    def test_refill_str(self):
        self.assertRaises(TypeError, self.vm.refill, "3")
    
    def test_refill_bool(self):
        self.assertRaises(TypeError, self.vm.refill, True)
    
    def test_refill_negative(self):
        self.assertRaises(ValueError, self.vm.refill, -1)

    def test_refill_greater_than_max(self):
        self.assertRaises(ValueError, self.vm.refill, 7)

#Postive TC
    def test_request_bottle_where_coinIsInserted(self):
        bottle = VendingMachine.Bottle()
        vendingMachine = VendingMachine.VendingMachine([bottle])
        vendingMachine.insert_coin()
        self.assertEqual(bottle,vendingMachine.request_bottle())

    def test_request_bottle_check_if_stack_decreases_now_stack_is_empty(self):
        bottle = VendingMachine.Bottle()
        vendingMachine = VendingMachine.VendingMachine([bottle])
        vendingMachine.insert_coin()
        vendingMachine.request_bottle()
        self.assertEqual(0,vendingMachine.get_size_of_stock())

    def test_request_bottle_check_if_stack_decreases_stack_is_not_empty(self):
        bottle = VendingMachine.Bottle()
        bottle2 = VendingMachine.Bottle()
        vendingMachine = VendingMachine.VendingMachine([bottle,bottle2])
        vendingMachine.insert_coin()
        vendingMachine.request_bottle()
        self.assertEqual(1,vendingMachine.get_size_of_stock())

#Negative TC

    def test_request_bottle_where_coinIsNotInserted_exception(self):
        vendingMachine = VendingMachine.VendingMachine()
        with self.assertRaises(Exception):
            vendingMachine.request_bottle()

    def test_request_bottle_twice_exception(self):
        bottle = VendingMachine.Bottle()
        bottle2 = VendingMachine.Bottle()
        vendingMachine = VendingMachine.VendingMachine([bottle,bottle2])
        vendingMachine.insert_coin()
        vendingMachine.request_bottle()
        with self.assertRaises(Exception):
            vendingMachine.request_bottle()
    
    def test_insertCoin_stockIsEmpty_exception(self):
        vendingMachine = VendingMachine.VendingMachine()
        with self.assertRaises(Exception):
            vendingMachine.insert_coin()

    def test_insertCoin_twice_exception(self):
        bottle = VendingMachine.Bottle()
        vendingMachine = VendingMachine.VendingMachine([bottle])
        vendingMachine.insert_coin()
        with self.assertRaises(Exception):
            vendingMachine.insert_coin()

if __name__ == '__main__':
    unittest.main()