# Audo added TEXT-123
# Copyright (c) 2026. All rights reserved.
# Licensed under the MIT License.
import algorithms


def example_algorithms():
    """
    Demonstrates the usage of bubble sort and binary search.
    """
    # Bubble Sort Example
    unsorted_data = [64, 34, 25, 12, 22, 11, 90]
    print(f"Unsorted Array: {unsorted_data}")
    algorithms.bubble_sort(unsorted_data)
    print(f"Sorted Array:   {unsorted_data}")

    # Binary Search Example
    target = 22
    result = algorithms.binary_search(unsorted_data, target)
    if result != -1:
        print(f"Element {target} is present at index {result}")
    else:
        print(f"Element {target} is not present in array")

def main():
    example_algorithms()

if __name__ == "__main__":
    main()