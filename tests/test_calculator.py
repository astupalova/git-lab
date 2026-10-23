"""Автоматические тесты учебного калькулятора."""
import io
import unittest
from unittest.mock import patch
from calculator import calculate, read_integer


class CalculatorTests(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(calculate(7, 3), 4)

    def test_negative_numbers(self):
        self.assertEqual(calculate(-7, 3), -10)

    def test_zero(self):
        self.assertEqual(calculate(0, 0), 0)

    def test_large_numbers(self):
        self.assertEqual(calculate(10**8, 10**8), 0)

    def test_invalid_input_prompts_again(self):
        with patch("builtins.input", side_effect=["oops", "-12"]):
            with patch("sys.stdout", new_callable=io.StringIO) as output:
                self.assertEqual(read_integer("Введите число: "), -12)
        self.assertIn("Ошибка", output.getvalue())


if __name__ == "__main__":
    unittest.main()
