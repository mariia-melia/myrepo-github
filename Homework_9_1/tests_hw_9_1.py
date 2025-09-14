import unittest
from homework_9_1 import (
    sum_function,
    return_longest_word,
    arithmetic_mean,
    sum_of_numbers_from_string,
    check_text_contains_h,
)

class TestFunctions(unittest.TestCase):

    # --- 1,2 tests for sum_function ---
    def test_01_sum_function_positive(self):
        self.assertEqual(sum_function([1, 2, 3]), 6)

    def test_02_sum_function_negative_numbers(self):
        self.assertEqual(sum_function([-5, 5, 10]), 10)

    # --- 3,4 tests for return_longest_word ---
    def test_03_longest_word(self):
        self.assertEqual(return_longest_word(["cat", "watermelon", "dog"]), "watermelon")

    def test_04_equal_length_words(self):
        self.assertIn(return_longest_word(["cat", "dog"]), ["cat", "dog"])
        # max поверне перше знайдене

    # --- 5,6 tests for arithmetic_mean ---
    def test_05_arithmetic_mean_positive(self):
        self.assertEqual(arithmetic_mean([2, 4, 6]), 4)

    def test_06_arithmetic_mean_float(self):
        self.assertAlmostEqual(arithmetic_mean([1, 2]), 1.5)

    # --- 7,8 tests for sum_of_numbers_from_string ---
    def test_07_sum_of_numbers_from_string_valid(self):
        self.assertEqual(sum_of_numbers_from_string("1,2,3"), 6)

    def test_08_sum_of_numbers_from_string_invalid(self):
        self.assertEqual(sum_of_numbers_from_string("1,a,3"), "Не можу це зробити!")

    # --- 9,10 tests for check_text_contains_h ---
    def test_09_check_text_contains_h_lowercase(self):
        self.assertEqual(check_text_contains_h("hello"), "Текст містить h/H")

    def test_10_check_text_contains_h_no_h(self):
        self.assertEqual(check_text_contains_h("world"), "Текст не містить h/H")


if __name__ == "__main__":
    unittest.main()