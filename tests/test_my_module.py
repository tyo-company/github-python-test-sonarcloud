# test_my_module.py
import unittest
from fastvector.my_module import Calculator, ConditionalProcessor

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(3, 5), 8)
        # This test only covers one case, not fully covering the method.

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(10, 7), 3)
        # This test only covers one case, not fully covering the method.

    # Removing test_multiply to make the coverage partial.

    def test_divide(self):
        self.assertEqual(self.calculator.divide(10, 2), 5)
        # This test covers one case but does not cover division by zero.

    def test_multiply_bug(self):
        self.assertEqual(self.calculator.multiply(3, 4), 12)
        # This test expects 12, but due to the bug, it will fail.

    # Removing test_divide_by_zero to make the coverage partial.
        
class TestConditionalProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = ConditionalProcessor()

    def test_process_for_1(self):
        self.assertEqual(self.processor.process(1), "Processed for 1")
        This test covers the condition for x == 1.

    def test_process_for_3(self):
        self.assertEqual(self.processor.process(3), "Processed for 3")
        # This test covers the condition for x == 3, but not for x == 2.

        
if __name__ == '__main__':
    unittest.main()
