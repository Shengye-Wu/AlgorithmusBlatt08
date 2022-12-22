import unittest
import selection_sort

class TestSelectionSort(unittest.TestCase):
    def test_a_normal_array(self):
        input_array = [3, 2, 1]
        selection_sort.selectionSort(input_array)
        self.assertEqual([1, 2, 3], input_array)
    def test_an_empty_array(self):
        input_array = []
        selection_sort.selectionSort(input_array)
        self.assertEqual([], input_array)
    def test_array_with_one_element(self):
        input_array = [42]
        selection_sort.selectionSort(input_array)
        self.assertEqual([42], input_array)
    def test_a_bigger_array_with_duplicates(self):
        input_array = [25, 42, 26, 42, 1, 41, 42, 40, 43]
        selection_sort.selectionSort(input_array)
        self.assertEqual([1, 25, 26, 40, 41, 42, 42, 42, 43], input_array)


if __name__ == '__main__':
    unittest.main()
