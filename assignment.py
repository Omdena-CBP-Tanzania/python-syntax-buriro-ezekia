# Part 1: Python Syntax (30 points)
"""

# Task 1: Function format_string(name, age)
def format_string(name, age):
    """
    Create a formatted string using f-strings.
    Return "My name is {name} and I am {age} years old".
    """
    return f"My name is {name} and I am {age} years old"

# Example usage
print(format_string("Buriro", 29))  # Output: My name is Alice and I am 30 years old

# Task 2: Function conditional_check(number)
def conditional_check(number):
    """
    Check if the number is greater than, less than, or equal to 10.
    Return "Greater", "Lesser", or "Equal" accordingly.
    """
    if number > 10:
        return "Greater"
    elif number < 10:
        return "Lesser"
    else:
        return "Equal"

# Example usage
print(conditional_check(15))  # Output: Greater
print(conditional_check(5))   # Output: Lesser
print(conditional_check(10))  # Output: Equal

# Task 3: Function loop_sum(n)
def loop_sum(n):
    """
    Use a loop to sum numbers from 1 to n.
    Return the sum.
    """
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Example usage
print(loop_sum(5))  # Output: 15 (1 + 2 + 3 + 4 + 5)

"""# Part 2: Data Structures (40 points)"""

# Task 1: Function list_operations(numbers)
def list_operations(numbers):
    """
    Take a list of numbers and return a tuple containing:
    - Sum of all numbers
    - Maximum number
    - Minimum number
    """
    # Calculate the sum of all numbers
    total_sum = sum(numbers)

    # Find the maximum number in the list
    max_number = max(numbers)

    # Find the minimum number in the list
    min_number = min(numbers)

    # Return the results as a tuple
    return (total_sum, max_number, min_number)

# Example usage
numbers = [1, 2, 3, 4, 5]
print(list_operations(numbers))  # Output: (15, 5, 1)

# Task 2: Function dict_operations(students_dict)
def dict_operations(students_dict):
    """
    Take a dictionary of student names and scores.
    Return a list of names of students who scored above 80.
    """
    # Initialize an empty list to store the names of students who scored above 80
    high_scorers = []

    # Iterate through the dictionary items
    for name, score in students_dict.items():
        # Check if the student's score is above 80
        if score > 80:
            # Add the student's name to the list
            high_scorers.append(name)

    # Return the list of high scorers
    return high_scorers

# Example usage
students_dict = {
    "Malima": 85,
    "Mwita": 75,
    "Wambura": 90,
    "David": 60
}
print(dict_operations(students_dict))  # Output: ['Malima', 'Wambura']

# ask 3: Function set_operations(list1, list2)
def set_operations(list1, list2):
    """
    Take two lists and return a set of common elements.
    """
    # Convert the lists to sets
    set1 = set(list1)
    set2 = set(list2)

    # Find the common elements between the two sets
    common_elements = set1.intersection(set2)

    # Return the set of common elements
    return common_elements

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(set_operations(list1, list2))  # Output: {4, 5}

"""# Part 3: Operators (30 points)"""

# Task 1: Function arithmetic_ops(a, b)
def arithmetic_ops(a, b):
    """
    Perform arithmetic operations on two numbers and return a dictionary with the results.

    Returns:
    - 'sum': a + b
    - 'difference': a - b
    - 'product': a * b
    - 'quotient': a / b (handle division by zero)
    """
    # Initialize the result dictionary
    results = {
        'sum': a + b,
        'difference': a - b,
        'product': a * b,
        'quotient': None if b == 0 else a / b
    }

    return results

# Example usage
print(arithmetic_ops(10, 5))  # Output: {'sum': 15, 'difference': 5, 'product': 50, 'quotient': 2.0}
print(arithmetic_ops(10, 0))  # Output: {'sum': 10, 'difference': 10, 'product': 0, 'quotient': None}

# Task 2: Function logical_ops(x, y)
def logical_ops(x, y):
    """
    Perform logical operations on two boolean values and return a dictionary with the results.

    Returns
    - 'and': x and y
    - 'or': x or y
    - 'not_x': not x
    """
    # Initialize the result dictionary
    results = {
        'and': x and y,
        'or': x or y,
        'not_x': not x
    }

    return results

# Example usage
print(logical_ops(True, False))  # Output: {'and': False, 'or': True, 'not_x': False}
print(logical_ops(False, False)) # Output: {'and': False, 'or': False, 'not_x': True}

# Task 3: Function bitwise_ops(a, b)
def bitwise_ops(a, b):
    """
    Perform bitwise operations on two integers and return a dictionary with the results.

    Returns
    - 'and': a & b
    - 'or': a | b
    - 'xor': a ^ b
    """
    # Initialize the result dictionary
    results = {
        'and': a & b,
        'or': a | b,
        'xor': a ^ b
    }

    return results

# Example usage:
print(bitwise_ops(10, 5))  # Output: {'and': 0, 'or': 15, 'xor': 15}
print(bitwise_ops(12, 7))  # Output: {'and': 4, 'or': 15, 'xor': 11}
