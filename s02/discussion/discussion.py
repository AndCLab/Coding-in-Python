# can be achieved using [ctrl + '/'] 
# Is a one line comment in python

"""
there is no keybind for writing mult-line 
comments but is still achievable using 
3 sets of quotation marks
"""

# Python syntax
# Displaying or Printing 
# Hello World in Python
print("Hello World")

# Variables
# Declaring variables
# No need to indicate the data type
# Can assign a value directly
age = 18

# In declaring a string [' or "] will work
middle_initial = "C"

# Naming convention should always start with a letter or an underscore '_'
# Initializing multiple variables
name1, name2, name3, name4 = "John", "Paul", "George", "Ringo"

# Data types in Python:
# Strings (str) - for alphanumeric and symbols
# Uses quotation marks (single or double)
full_name = "John Doe"
secret_code = "Pa$$word"

# Numbers (int, float, complex)
# Integers has no decimals or quotation marks
# Float uses decimals
# Complex numbers uses j as an imaginary number
num_of_days = 365 
pi_approx = 3.1416
complex_num = 1 + 5j

# Boolean (bool) data type - truth values
# First letter should be in upper case for True and False
isLearning = True 
isDifficult = False

# Using the variables print a message:
print("My name is " + full_name)

# Typecasting:
# Printing an int uses typecasting [str(int_variable)] or fstring [print(f"sentence {int_variable}")]
# int() - converts the value to integer value
# float() - converts the value into float value
# str() - converts the value into string
print("My age is " + str(age))
print(int(3.5))
print(int("9861"))
# F-strings (adding a lowercase 'f' before the string and place the variable in curly brackets)
print(f"My age is {age}")
print(f"Hi, my name is {full_name} and my age is {age}")

# Operations
# Addition - '+'
print(1 + 10)
# Subtraction - '-'
print(15 - 8) 
# Multiplication - '*'
print(18 * 9)
# Division - '/'
print(21 / 7)
# Modulo or remainder - '%'
print(18 % 4)
# Exponent - '**'
print(2 ** 6)

# Assignment Operators 
# assigns a value to a avariable
num1 = 3
# changing value using addition assignment operator ['+=/] num1 = num1 + 4
num1 += 4
print(num1)
# Subtraction assignment
num1 -= 4
print(num1)
# Multiplication assignment
num1 *= 4
print(num1)
# Division assignment
num1 /= 4
print(num1)

# Comparison operators - used to compare values (returns a boolean value)
# Comparing should return True or False
print(1 == 1)
print(5 > 10)
print(5 < 10)
print(1 <= 1)
print(2 >= 3)
print(1 != 1)

# Logical operators
# and Logical operator will only return True if both are True, otherwise False
print(True and False)
# or Logical operator will only return False if both are False, otherwise True
print(True or False)
# not Logical operator will negate the given value
print(not False)

