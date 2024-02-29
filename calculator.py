"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

#check first item of the list
#use that to map to the functions in arithmetic.py
#call the function on the other list elements 

user_input = input("Enter your equation > ")
tokens = user_input.split(' ')

if tokens[0] == "q":
    quit
else:
    if tokens[0] == "+":
        print(add(tokens[1],tokens[2]))
    elif tokens[0] == "-":
        print(subtract(tokens[1],tokens[2]))
    elif tokens[0] == "*":
        print(multiply(tokens[1],tokens[2]))
    elif tokens[0] == "/":
        print(divide(tokens[1],tokens[2]))
    elif tokens[0] == "square":
        print(square(tokens[1]))

# Replace this with your code
