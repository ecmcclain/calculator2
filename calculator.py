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
    

# Replace this with your code
