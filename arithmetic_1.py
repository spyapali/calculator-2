# def add(num1, num2):
#     return num1 + num2

def add_many(list_of_numbers):
    result = 0
    for i in list_of_numbers:
        result = result + i
    return result



def subtract(list_of_numbers):
    result = 0
    for i in list_of_numbers:
        result = result - i
    return result


def multiply(list_of_numbers):
    result = 0
    for i in list_of_numbers:
        result = result * i
    return result


def divide(num1, num2):
    return float(num1) / float(num2)
    # Need to turn at least argument to float for division to
    # not be integer division


def square(num1):
    # Needs only one argument
    return num1 * num1


def cube(num1):
    # Needs only one argument
    return num1 * num1 * num1


def power(num1, num2):
    return num1 ** num2  # ** = exponent operator


def mod(list_of_numbers):
    result = 0
    for i in list_of_numbers:
        result = result % i
    return result
    
