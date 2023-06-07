import unittest
from sayTheNumber import sayNumber


class SayNumberTestCase(unittest.TestCase):

    def test_invalid_input_type(self):
        # Test case to validate input type and error handling
        with self.assertRaises(ValueError):
            sayNumber("123")

    def test_single_digits(self):
        # Test case for single digit numbers
        self.assertEqual(sayNumber(0), "zero")
        self.assertEqual(sayNumber(1), "one")
        self.assertEqual(sayNumber(9), "nine")

    def test_double_digits_less_than_20(self):
        # Test case for double digit numbers less than 20
        self.assertEqual(sayNumber(10), "ten")
        self.assertEqual(sayNumber(11), "eleven")
        self.assertEqual(sayNumber(19), "nineteen")

    def test_double_digits_greater_than_20(self):
        # Test case for double digit numbers greater than or equal to 20
        self.assertEqual(sayNumber(20), "twenty")
        self.assertEqual(sayNumber(21), "twenty-one")
        self.assertEqual(sayNumber(99), "ninety-nine")

    def test_triple_digits(self):
        # Test case for triple digit numbers
        self.assertEqual(sayNumber(100), "one hundred")
        self.assertEqual(sayNumber(123), "one hundred and twenty-three")
        self.assertEqual(sayNumber(999), "nine hundred and ninety-nine")

    def test_four_or_more_digits(self):
        # Test case for numbers with four or more digits
        self.assertEqual(sayNumber(1000), "one thousand")
        self.assertEqual(sayNumber(20000), "twenty thousand")
        self.assertEqual(sayNumber(1033286), "one million, thirty-three thousand, two hundred and eighty-six")
        self.assertEqual(sayNumber(12000013), "twelve million and thirteen")
        self.assertEqual(sayNumber(90376000010012), "ninety trillion, three hundred and seventy-six billion, ten thousand and twelve")

    def test_invalid_input(self):
        # Test case for negative numbers
        self.assertEqual(sayNumber(-1), "No Number to Say!")


if __name__ == '__main__':
    unittest.main()
