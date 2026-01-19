# Audo added TEXT-123
# Copyright (c) 2026. All rights reserved.
# Licensed under the MIT License.

from typing import List, TypeVar, Optional

T = TypeVar('T')

def bubble_sort(arr: List[T]) -> None:
    """
    Sorts an array using the bubble sort algorithm.
    :param arr: List of elements to be sorted
    :return: None (sorts in-place)
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

def binary_search(arr: List[int], target: int) -> int:
    """
    Searches for a target value in a sorted array using binary search.
    :param arr: Sorted list of elements
    :param target: Value to search for
    :return: Index of target if found, else -1
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1
