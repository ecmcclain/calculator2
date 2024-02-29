"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

#check first item of the list
#use that to map to the functions in arithmetic.py
#call the function on the other list elements 

while True:
    user_input = input("Enter your equation > ")
    temp = user_input.split(' ')

    if len(temp) == 3:
        tokens = [temp[0], int(temp[1]), int(temp[2])]
    elif len(temp) == 2:
        tokens = [temp[0], int(temp[1])]
    elif len(temp) == 1:
        tokens = temp[0]

    if tokens[0] == "q":
        break
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
        elif tokens[0] == "cube":
            print(cube(tokens[1]))
        elif tokens[0] == "pow":
            print(power(tokens[1],tokens[2]))
        elif tokens[0] == "mod":
            print(mod(tokens[1],tokens[2]))

# Replace this with your code
