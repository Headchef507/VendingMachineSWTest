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

if __name__ == '__main__':
    unittest.main()