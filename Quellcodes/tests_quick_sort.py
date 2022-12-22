import unittest
import quick_sort

class MyTestCase(unittest.TestCase):
    def test_a_normal_array(self):
        input_array = [3, 2, 1]
        input_array = quick_sort.quickSort(input_array)
        self.assertEqual([1, 2, 3], input_array)

    def test_an_empty_array(self):
        input_array = []
        input_array = quick_sort.quickSort(input_array)
        self.assertEqual([], input_array)

    def test_array_with_one_element(self):
        input_array = [42]
        input_array = quick_sort.quickSort(input_array)
        self.assertEqual([42], input_array)

    def test_a_bigger_array_with_duplicates(self):
        input_array = [25, 42, 26, 42, 1, 41, 42, 40, 43]
        input_array = quick_sort.quickSort(input_array)
        self.assertEqual([1, 25, 26, 40, 41, 42, 42, 42, 43], input_array)

if __name__ == '__main__':
    unittest.main()
