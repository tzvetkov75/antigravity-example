# Audo added TEXT-123
# Copyright (c) 2026. All rights reserved.
# Licensed under the MIT License.
import algorithms
import database_operations # type: ignore


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

def example_database_operations():
    """
    Demonstrates usage of database operations (requires DB credentials).
    """
    print("\n--- Database Operations Example ---")
    connection = database_operations.get_db_connection()
    if connection:
        database_operations.create_table_if_not_exists(connection)
        database_operations.add_user(connection, "PETER PERTERSON", "peter@test.com", "test_password")
        connection.close()
    else:
        print("Skipping database operations (no connection).")

def main():
    example_algorithms()
    example_database_operations()

if __name__ == "__main__":
    main()