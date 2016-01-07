"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *



new_numbers = raw_input("Please enter operator, followed by one or two numbers.")
user_input = new_numbers.split(" ")
# print user_input
#while len(user_input) > 0:

if user_input[0] == "q":
    print "Good bye"


elif len(user_input) == 2:
    operator = user_input[0]
    num1 = int(user_input[1])
    if operator == "square":
        print square(num1)

    elif operator == "cube":
        print cube(num1)


elif len(user_input) == 3:
    operator = user_input[0]
    num1 = int(user_input[1])
    num2 = int(user_input[2])

    if operator == "+":
        print add(num1, num2)

    elif operator == "-":
        print subtract(num1, num2)

    elif operator == "*":
        print multiply(num1, num2)

    elif operator == "power":
        print power(num1, num2)

    elif operator == "/":
        print divide(num1, num2)

    elif operator == "%":
        print mod(num1, num2)



