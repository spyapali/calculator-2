"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic_1 import *


# take in any number of inputs = within the while loop. 

# def read_input():
#     new_numbers = raw_input("Please enter operator, followed by one or two numbers.")
#     user_input = new_numbers.split(" ")

new_numbers = raw_input("Please enter operator, followed by one or two numbers.")
user_input = new_numbers.split(" ")
# print user_input
#while len(user_input) > 0:

# one function that reads in the file/input and it's making it a list of strings. Based on the operator, decide where to go. 



if user_input[0] == "q":
    print "Good bye"
 

elif len(user_input) == 2:
    operator = user_input[0]
    num1 = int(user_input[1])
    if operator == "square":
        print square(num1)

    elif operator == "cube":
        print cube(num1)

elif user_input[0] == "power":
    operator = user_input[0]
    num1 = float(user_input[1])
    num2 = float(user_input[2])
    print power(num1, num2)

elif user_input[0] == "/":
    operator = user_input[0]
    num1 = float(user_input[1])
    num2 = float(user_input[2])
    print divide(num1, num2)


# elif user_input[0] == "/":
#     operator = user_input[0]
#     numbers_in_string = user_input[1:]
#     list_of_numbers = []

#     for num in numbers_in_string:
#         list_of_numbers.append(float(num))

#     print divide(list_of_numbers)

elif len(user_input) > 2:
    operator = user_input[0]
    numbers_in_string = user_input[1:]
    list_of_numbers = []


    for num in numbers_in_string:
        list_of_numbers.append(int(num))

    if operator == "+":
        print add_many(list_of_numbers)

    elif operator == "-":
        print subtract(list_of_numbers)

    elif operator == "*":
        print multiply(list_of_numbers)



    elif operator == "%":
        print mod(list_of_numbers)



