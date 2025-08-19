# ============================
# mmn13_tester.py - Tester for mmn13.py
# ============================

from mmn13 import *

def print_result(desc, result):
    print(f"{desc}: {result}")


def test_complement():
    print("\n--- Testing complement ---")

    # [2, 3, 6]
    print_result("Test 1", complement([9, 8, 7, 5, 4, 1]))

    # []
    print_result("Test 2", complement([1, 4, 2, 3]))

    # []
    print_result("Test 3", complement([]))

    # [1, 3, 5]
    print_result("Test 4", complement([2, 4, 6]))

    # [2, 3, 4, 5, 6, 7, 8, 9]
    print_result("Test 5", complement([10, 1]))


def test_shift_k_right():
    print("\n--- Testing shift_k_right ---")

    # [3, 4, 5, 1, 2]
    print_result("Test 1", shift_k_right([1, 2, 3, 4, 5], 3))

    # [5, 1, 2, 3, 4]
    print_result("Test 2", shift_k_right([1, 2, 3, 4, 5], 1))

    try:
        # Should raise ValueError
        shift_k_right([1, 2], 5)
    except ValueError as e:
        # Exception caught: ...
        print_result("Test 3", f"\nException caught:\n{e}")


def test_shift_right_size():
    print("\n--- Testing shift_right_size ---")

    a = [4, -1, 9, 7, 11, 2]
    b = [11, 2, 4, -1, 9, 7]

    # Shouldn't the following be expected to be 2
    # rather than 4?
    print_result("Test 1", shift_right_size(a, b))  # 4

    c = [4, -1, 9, 7, 11, 2]
    d = [4, -1, 7, 9, 11, 2]

    print_result("Test 2", shift_right_size(c, d))  # None

    print_result(
        "Test 3",
        shift_right_size([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))  # 0

    # Shouldn't the following be expected
    # to be 2 rather than 3?
    print_result(
        "Test 4",
        shift_right_size([1, 2, 3, 4, 5], [4, 5, 1, 2, 3]))  # 3

    print_result(
        "Test 5",
        shift_right_size([1, 2, 3, 4, 5], [1, 2, 3, 5, 4]))  # None


def test_is_perfect():
    print("\n--- Testing is_perfect ---")

    print_result(
        "Test 1", is_perfect([2, 3, 2, 3, 0]))  # False

    print_result(
        "Test 2", is_perfect([2, 3, 2, 1, 0]))  # False

    print_result(
        "Test 3", is_perfect([]))               # True

    print_result(
        "Test 4", is_perfect([1, 2, 3, 4, 0]))  # True

    try:
        is_perfect([2, 3, "a", 0])
    except TypeError as e:
        # Exception caught: ...
        print_result("Test 5", f"Exception caught: {e}")


def test_identity_matrix():
    print("\n--- Testing identity_matrix ---")

    mat1 = [[1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1]]

    print_result(
        "Test 1", identity_matrix(mat1))  # True

    mat2 = [[1, 0, 0],
            [0, 1, 0],
            [0, 0, 1.0]]

    try:
        identity_matrix(mat2)
    except TypeError as e:
        # Exception caught: Not all values are int
        print_result("Test 2", f"Exception caught: {e}")


def test_create_sub_matrix():
    print("\n--- Testing create_sub_matrix ---")

    mat = [[1, 0, 0, 0, 0],
           [0, 1, 0, 0, 0],
           [0, 0, 1, 0, 0],
           [0, 0, 0, 1, 0],
           [1, 0, 0, 0, 1]]

    # 3x3 identity center
    print_result("Test 1", create_sub_matrix(mat, 3))

    mat_bad = [[1, 0], [0, 1, 0]]

    try:
        create_sub_matrix(mat_bad, 1)
    except IndexError as e:
        # Exception caught: Not all rows are equal
        print_result("Test 2", f"Exception caught: {e}")


def test_max_identity_matrix():
    print("\n--- Testing max_identity_matrix ---")

    mat1 = [[1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [1, 0, 0, 0, 1]]

    print_result(
        "Test 1", max_identity_matrix(mat1))  # 3

    mat2 = [[1, 0, 0],
            [0, 1, 0],
            [0, 0, 1.0]]

    # Not all values are int
    # Test 2: 0
    print_result("Test 2", max_identity_matrix(mat2))

    mat3 = [[1, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 1]]

    print_result(
        "Test 3", max_identity_matrix(mat3))  # 1


if __name__ == "__main__":
    test_complement()
    test_shift_k_right()
    test_shift_right_size()
    test_is_perfect()
    test_identity_matrix()
    test_create_sub_matrix()
    test_max_identity_matrix()