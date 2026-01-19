# Audo added TEXT-123
# Copyright (c) 2026. All rights reserved.
# Licensed under the MIT License.
import unittest
from unittest.mock import patch, call
from io import StringIO
import main

class TestMain(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    @patch('algorithms.bubble_sort')
    @patch('algorithms.binary_search')
    def test_example_algorithms(self, mock_binary_search, mock_bubble_sort, mock_stdout):
        # Setup mocks
        mock_bubble_sort.return_value = [11, 12, 22, 25, 34, 64, 90] # Actually bubble_sort modifies in-place, but let's just check call
        mock_binary_search.return_value = 4
        
        main.example_algorithms()
        
        # Verify bubble_sort called
        unsorted_data = [64, 34, 25, 12, 22, 11, 90]
        # Note: Since bubble_sort modifies in place in the actual code, 
        # checking the exact argument might be tricky if we didn't mock it to NOT modify it
        # But here we mocked it completely, so it shouldn't modify the list passed to it unless we configured side_effect
        # wait, the code in main.py passes unsorted_data. 
        # mock_bubble_sort(unsorted_data) is called.
        
        self.assertTrue(mock_bubble_sort.called)
        
        # Verify binary_search called
        mock_binary_search.assert_called_with(unsorted_data, 22)
        
        # Verify output
        output = mock_stdout.getvalue()
        self.assertIn("Unsorted Array:", output)
        self.assertIn("Sorted Array:", output)
        self.assertIn("Element 22 is present at index 4", output)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('algorithms.binary_search')
    def test_example_algorithms_not_found(self, mock_binary_search, mock_stdout):
        # Setup mocks to simulate not found
        # We need to mock bubble_sort as well to avoid actual execution if we want to be pure unit test
        with patch('algorithms.bubble_sort'):
            mock_binary_search.return_value = -1
            
            main.example_algorithms()
            
            output = mock_stdout.getvalue()
            # The target is hardcoded to 22 in main.py, so we can't easily test 'not found' path 
            # unless we change main.py or if binary_search returns -1 for 22 (which we forced here)
            self.assertIn("Element 22 is not present in array", output)

if __name__ == '__main__':
    unittest.main()
