import unittest
import VendingMachine


class testVendingMachine(unittest.TestCase):
    def setUp(self) -> None:
        pass

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
        vm = VendingMachine.VendingMachine(5)
        vm.refill(5)
        self.assertEqual(vm.get_stock(), 10, "Should be 10")

    def test_refill3(self):
        vm = VendingMachine.VendingMachine(5)
        vm.refill(3)
        self.assertEqual(vm.get_stock(), 8, "Should be 8")
    
    def test_refill_str(self)

if __name__ == '__main__':
    unittest.main()