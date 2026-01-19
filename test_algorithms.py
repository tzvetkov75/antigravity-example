# Audo added TEXT-123
# Copyright (c) 2026. All rights reserved.
# Licensed under the MIT License.
import unittest
from algorithms import bubble_sort, binary_search

class TestAlgorithms(unittest.TestCase):
    def test_bubble_sort_normal(self):
        data = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]
        bubble_sort(data)
        self.assertEqual(data, expected)

    def test_bubble_sort_sorted(self):
        data = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        bubble_sort(data)
        self.assertEqual(data, expected)

    def test_bubble_sort_reverse(self):
        data = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]
        bubble_sort(data)
        self.assertEqual(data, expected)

    def test_bubble_sort_empty(self):
        data = []
        expected = []
        bubble_sort(data)
        self.assertEqual(data, expected)

    def test_bubble_sort_single(self):
        data = [1]
        expected = [1]
        bubble_sort(data)
        self.assertEqual(data, expected)

    def test_binary_search_found(self):
        data = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(data, 3), 2)
        self.assertEqual(binary_search(data, 1), 0)
        self.assertEqual(binary_search(data, 5), 4)

    def test_binary_search_not_found(self):
        data = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(data, 6), -1)
        self.assertEqual(binary_search(data, 0), -1)

    def test_binary_search_empty(self):
        data = []
        self.assertEqual(binary_search(data, 1), -1)

    def test_bubble_sort_invalid_input(self):
        # Test with non-list input
        with self.assertRaises(TypeError):
            bubble_sort(123)
        with self.assertRaises(TypeError):
            bubble_sort(None)

    def test_bubble_sort_mixed_types(self):
        # Test with mixed types that cannot be compared
        data = [1, "2", 3]
        with self.assertRaises(TypeError):
            bubble_sort(data)

    def test_binary_search_invalid_input(self):
        # Test with non-list input
        with self.assertRaises(TypeError):
            binary_search(123, 1)
        with self.assertRaises(TypeError):
            binary_search(None, 1)

if __name__ == '__main__':
    unittest.main()
