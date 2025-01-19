import pytest
from assignment import *

# Part 1: Python Syntax (30 points)

# Task 1: Function format_string(name, age)
def test_format_string():
    """
    Test the format_string function with different inputs.
    """
    assert format_string("Buriro", 29) == "My name is Buriro and I am 29 years old"
    assert format_string("Ezekia", 25) == "My name is Ezekia and I am 25 years old"
    assert format_string("", 0) == "My name is  and I am 0 years old"

# Task 2: Function conditional_check(number)
def test_conditional_check():
    """
    Test the conditional_check function with different inputs.
    """
    assert conditional_check(15) == "Greater"
    assert conditional_check(5) == "Lesser"
    assert conditional_check(10) == "Equal"

# Task 3: Function loop_sum(n)
def test_loop_sum():
    """
    Test the loop_sum function with different inputs.
    """
    assert loop_sum(5) == 15  # 1 + 2 + 3 + 4 + 5
    assert loop_sum(0) == 0
    assert loop_sum(1) == 1

# Part 2: Data Structures (40 points)

# Task 1: Function list_operations(numbers)
def test_list_operations():
    """
    Test the list_operations function with different inputs.
    """
    numbers = [1, 2, 3, 4, 5]
    assert list_operations(numbers) == (15, 5, 1)
    assert list_operations([]) == (0, None, None)  # Handle empty list

# Task 2: Function dict_operations(students_dict)
def test_dict_operations():
    """
    Test the dict_operations function with different inputs.
    """
    students_dict = {
        "Malima": 85,
        "Mwita": 75,
        "Wambura": 90,
        "David": 60
    }
    assert dict_operations(students_dict) == ['Malima', 'Wambura']
    assert dict_operations({}) == []  # Handle empty dictionary

# Task 3: Function set_operations(list1, list2)
def test_set_operations():
    """
    Test the set_operations function with different inputs.
    """
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    assert set_operations(list1, list2) == {4, 5}
    assert set_operations([], []) == set()  # Handle empty lists

# Part 3: Operators (30 points)

# Task 1: Function arithmetic_ops(a, b)
def test_arithmetic_ops():
    """
    Test the arithmetic_ops function with different inputs.
    """
    assert arithmetic_ops(10, 5) == {'sum': 15, 'difference': 5, 'product': 50, 'quotient': 2.0}
    assert arithmetic_ops(10, 0) == {'sum': 10, 'difference': 10, 'product': 0, 'quotient': None}
    assert arithmetic_ops(-10, -5) == {'sum': -15, 'difference': -5, 'product': 50, 'quotient': 2.0}

# Task 2: Function logical_ops(x, y)
def test_logical_ops():
    """
    Test the logical_ops function with different inputs.
    """
    assert logical_ops(True, False) == {'and': False, 'or': True, 'not_x': False}
    assert logical_ops(False, False) == {'and': False, 'or': False, 'not_x': True}
    assert logical_ops(True, True) == {'and': True, 'or': True, 'not_x': False}

# Task 3: Function bitwise_ops(a, b)
def test_bitwise_ops():
    """
    Test the bitwise_ops function with different inputs.
    """
    assert bitwise_ops(10, 5) == {'and': 0, 'or': 15, 'xor': 15}
    assert bitwise_ops(12, 7) == {'and': 4, 'or': 15, 'xor': 11}
    assert bitwise_ops(0, 0) == {'and': 0, 'or': 0, 'xor': 0}
