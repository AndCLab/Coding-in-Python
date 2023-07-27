# Input:
# Input() allows users to gather data from user input
# it returns "string" data type:
# username = input("please enter your name: \n")
# print(f"Hi {username}! Welcome to Python Short Course!")

# Input for an integer
# adding two numbers
# Use type casting to convert string input to int
# num1 = int(input("Enter 1st number: \n"))
# num2 = int(input("Enter 2nd number: \n"))
# print(f"The sum of num1 and num2 is {num1 + num2}")

# Conditions:
# If-else statements
# used to choose between two or more code blocks depending on the condition
# Declare a variable to use for the conditional statement
# Indentions are used to separate code blocks
# Indentions are important - python does not use curly-braces
# test_num = 75
# if test_num >= 60:
# 	print("Test Passed")
# else:
# 	print("test Failed")

# Else-If chains
# Used in between if and else
# is just an added if statement 
# dependent on the first if statement
# elif stands for "else if"
# test_num2 = int(input("Please enter the 2nd test number: \n"))
# if test_num2 > 0:
# 	print("The number is positive")
# elif test_num2 == 0:
# 	print("The number is zero")
# else:
# 	print("The number is negative")

# Mini-Exercise
# Create an if-else statement that determines if a number is divisible by 3, 5 or both
# If the number is divisible by 3, print "The number is divisible by 3"
# If the number is divisible by 5, print "The number is divisible by 5"
# If the number is divisible by 5 and 3, print "The number is divisible by both 3 and 5"
# If the number is not divisible by any, print "The number is not divisible by 3 nor 5"
# test_num3 = int(input("Enter the number: \n"))
# if test_num3%3 == 0 and test_num3%5 == 0:
# 	print("The number is divisible by both 3 and 5")
# elif test_num3%3 == 0:
# 	print("The number is divisible by 3")
# elif test_num3%5 == 0:
# 	print("The number is divisible by 5")
# else:
# 	print("The number is not divisble by 3 nor 5")

# Repetition Control Structures
# Loops: Repeating blocks of code
# While loops are used to execute a set of statements as long as the condition is true
# i = 1
# while i <= 5:
# 	print(f"Current count of i is {i}")
# 	i += 1

# Foor loops are used for iterating over a sequence
# indiv_fruit represents the elements inside the array fruit
# fruits = ["apple", "banana", "cherry"]
# for indiv_fruit in fruits:
# 	print(indiv_fruit)

# range() method
# To use the for loop to iterate through values, the range method is used
# range() by default is 0 as a starting value
# range() parameter which is 6 in the example indicates when range will stop
# range increments the default value which is 0 inside the loop
# for x in range(6):
# 	print(f"The current value is {x}")

# range() has multiple arguments:
# range(starting_value, stop_value)
# for x in range(6, 10):
#  	print(f"The current value is {x}")

# range(starting_value, stope_value, increment_value)
# for x in range(6, 10, 2):
#  	print(f"The current value is {x}")

# Break Statements:
# Break is used to stop the loop
# Break inside a nested while loop will still stop the main loop
# j = 1
# while j < 6:
# 	print(j)
# 	if j == 3:
# 		break
# 	j += 1

# Continue Statements:
# Continue skips an interation in a loop
# continue returns the control to the beginning of the while loop and continues with the iteration
k = 1
while k < 6:
	k += 1
	if k == 3:
		continue
	print(k)

