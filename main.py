# Audo added TEXT-123
from algorithms import binary_search, bubble_sort

def example_algorithms():
    """
    Demonstrates usage of binary search and bubble sort.
    """
    # Bubble Sort Example
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    print(f"Unsorted list: {unsorted_list}")
    bubble_sort(unsorted_list)
    print(f"Sorted list: {unsorted_list}")

    # Binary Search Example
    target = 22
    result = binary_search(unsorted_list, target)
    if result != -1:
        print(f"Element {target} is present at index {result}")
    else:
        print(f"Element {target} is not present in array")

    target_missing = 100
    result_missing = binary_search(unsorted_list, target_missing)
    if result_missing != -1:
        print(f"Element {target_missing} is present at index {result_missing}")
    else:
        print(f"Element {target_missing} is not present in array")

def main():
    example_algorithms()

if __name__ == "__main__":
    main()
