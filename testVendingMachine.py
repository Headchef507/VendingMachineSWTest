import unittest
import VendingMachine


class testVendingMachine(unittest.TestCase):
    def setUp(self):
     #   self.vm = VendingMachine.VendingMachine(5)
        self.bottle1 = VendingMachine.Bottle()
        self.bottle2 = VendingMachine.Bottle()
        self.bottle3 = VendingMachine.Bottle()
        self.bottle4 = VendingMachine.Bottle()
        self.bottle5 = VendingMachine.Bottle()
        self.bottle6 = VendingMachine.Bottle()
        self.bottle7 = VendingMachine.Bottle()
        self.bottle8 = VendingMachine.Bottle()
        self.bottle9 = VendingMachine.Bottle()
        self.bottle10 = VendingMachine.Bottle()

    # def test_sum(self):
        # self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")
    
    def test_empty_stock_is_zero(self):
        empty_vm = VendingMachine.VendingMachine()
        self.assertEqual(empty_vm.get_size_of_stock(), 0, "Should be 0")
    
    def test_5_stock_is_5(self):
        btl_lst = [self.bottle1, self.bottle2, self.bottle3, self.bottle4, self.bottle5]
        five_vm = VendingMachine.VendingMachine(btl_lst)
        self.assertEqual(five_vm.get_size_of_stock(), 5, "Should be 5")
    
    def test_negative_init(self):
        self.assertRaises(TypeError, VendingMachine.VendingMachine, -1)

    def test_non_int_init(self):
        self.assertRaises(TypeError, VendingMachine.VendingMachine, "3")
    
    def test_max_init(self):
        bottle11 = VendingMachine.Bottle()
        # self.assertEqual(0, )
        eleven_lst = [self.bottle1, self.bottle2, self.bottle3, self.bottle4, self.bottle5, self.bottle6, self.bottle7, self.bottle8, self.bottle9, self.bottle10, bottle11]
        self.assertRaises(IndexError, VendingMachine.VendingMachine, eleven_lst)

    def test_refill5(self):
        lst = [self.bottle1, self.bottle2, self.bottle3, self.bottle4, self.bottle5]
        vm = VendingMachine.VendingMachine(lst)
        five_lst = [self.bottle6, self.bottle7, self.bottle8, self.bottle9, self.bottle10]
        self.assertEqual(vm.get_size_of_stock(), len(five_lst), "Should be 10")
        del vm

    def test_refill3(self):
        three_lst = [self.bottle1, self.bottle2, self.bottle3]
        five_lst = [self.bottle4, self.bottle5, self.bottle6, self.bottle7, self.bottle8]
        vm = VendingMachine.VendingMachine(five_lst)
        vm.refill(three_lst)
        self.assertEqual(vm.get_size_of_stock(), 8, "Should be 8")
        del vm
    
    def test_refill_str(self):
        vm = VendingMachine.VendingMachine()
        self.assertRaises(TypeError, vm.refill, "3")
        del vm
    
    def test_refill_bool(self):
        vm_test_refill_bool = VendingMachine.VendingMachine()
        self.assertRaises(TypeError, vm_test_refill_bool.refill, True)
        del vm_test_refill_bool
    
    def test_refill_negative(self):
        vm = VendingMachine.VendingMachine()
        self.assertRaises(TypeError, vm.refill, -1)
        del vm

    def test_refill_greater_than_max(self):
        vm = VendingMachine.VendingMachine()
        self.assertRaises(TypeError, vm.refill, 7)
        del vm

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