# Part 1: Python Syntax (30 points)

# Task 1: Function format_string(name, age)
def format_string(name, age):
    """
    Create a formatted string using f-strings.
    
    Parameters:
    name (str): The name of the person.
    age (int): The age of the person.
    
    Returns:
    str: A formatted string.
    """
    return f"My name is {name} and I am {age} years old"

# Example usage
print(format_string("Buriro", 29))  # Output: My name is Buriro and I am 29 years old

# Task 2: Function conditional_check(number)
def conditional_check(number):
    """
    Check if the number is greater than, less than, or equal to 10.
    
    Parameters:
    number (int): The number to check.
    
    Returns:
    str: "Greater", "Lesser", or "Equal" accordingly.
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
    
    Parameters:
    n (int): The upper limit of the range.
    
    Returns:
    int: The sum of numbers from 1 to n.
    """
    total_sum = 0
    for number in range(1, n + 1):
        total_sum += number
    return total_sum

# Example usage
print(loop_sum(5))  # Output: 15 (1 + 2 + 3 + 4 + 5)

# Part 2: Data Structures (40 points)

# Task 1: Function list_operations(numbers)
def list_operations(numbers):
    """
    Take a list of numbers and return a tuple containing:
    - Sum of all numbers
    - Maximum number
    - Minimum number
    
    Parameters:
    numbers (list): The list of numbers.
    
    Returns:
    tuple: A tuple containing the sum, maximum, and minimum numbers.
    """
    if not numbers:  # Check if the list is empty
        return (0, None, None)

    total_sum = sum(numbers)
    max_number = max(numbers)
    min_number = min(numbers)
    return (total_sum, max_number, min_number)

# Example usage
numbers = [1, 2, 3, 4, 5]
print(list_operations(numbers))  # Output: (15, 5, 1)

# Task 2: Function dict_operations(students_dict)
def dict_operations(students_dict):
    """
    Take a dictionary of student names and scores.
    Return a list of names of students who scored above 80.
    
    Parameters:
    students_dict (dict): A dictionary where keys are student names and values are their scores.
    
    Returns:
    list: A list of names of students who scored above 80.
    """
    high_scorers = []
    for name, score in students_dict.items():
        if score > 80:
            high_scorers.append(name)
    return high_scorers

# Example usage
students_dict = {
    "Malima": 85,
    "Mwita": 75,
    "Wambura": 90,
    "David": 60
}
print(dict_operations(students_dict))  # Output: ['Malima', 'Wambura']

# Task 3: Function set_operations(list1, list2)
def set_operations(list1, list2):
    """
    Take two lists and return a set of common elements.
    
    Parameters:
    list1 (list): The first list of elements.
    list2 (list): The second list of elements.
    
    Returns:
    set: A set of common elements.
    """
    return set(list1) & set(list2)

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(set_operations(list1, list2))  # Output: {4, 5}

# Part 3: Operators (30 points)

# Task 1: Function arithmetic_ops(a, b)
def arithmetic_ops(a, b):
    """
    Perform arithmetic operations on two numbers and return a dictionary with the results.
    
    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.
    
    Returns:
    dict: A dictionary with the results of sum, difference, product, and quotient.
    """
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
    
    Parameters:
    x (bool): The first boolean value.
    y (bool): The second boolean value.
    
    Returns:
    dict: A dictionary with the results of 'and', 'or', and 'not_x'.
    """
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
    
    Parameters:
    a (int): The first integer.
    b (int): The second integer.
    
    Returns:
    dict: A dictionary with the results of 'and', 'or', and 'xor'.
    """
    results = {
        'and': a & b,
        'or': a | b,
        'xor': a ^ b
    }
    return results

# Example usage:
print(bitwise_ops(10, 5))  # Output: {'and': 0, 'or': 15, 'xor': 15}
print(bitwise_ops(12, 7))  # Output: {'and': 4, 'or': 15, 'xor': 11}
