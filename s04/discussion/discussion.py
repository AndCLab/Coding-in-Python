# Lists 
# Lists are similar to arrays in JavaScript in a sense that they can contain a collection of data
# To create a list, the square bracket ([]) is used.
names = ["John", "Paul", "George", "Ringo"]
programs = ['developer career', 'pi-shape', 'short courses']
durations = [260, 180, 20]
truth_values = [True, False, True, True, False]

# Example of a list with different data types
sample_list = ["Apple", 3, False, "Potato", 4, True] 
print(sample_list)

# Getting the size or the number of elements of the list
print(len(programs))

# Access values of the list
# By using the index number of the element 
# Access the first item/element in the list
print(programs[0]) 
# Access the second item/element in the list
print(durations[1])
# Access the second item/element in the list
print(programs[-1])
# Access the whole list/all elements
print(durations)
# Access a range of values 
# list [start index: end index]
# programs[starts at 0: access 2 items]
# end index is not included in accessong
print(programs[0:2])

# Updating the list 
# Print the current value 
print(f'Current value: {programs[2]}')
# Update the value by accessing the programs list
programs[2] = 'Short Courses XD'
# After updating the element print the new value
print(f'New value: {programs[2]}')

# Mini-exercise
# 1. Create a list of names of 5 students
# 2. Create a list of grades for the 5 students
# 3. Use a loop to iterate through the lists printing in following format:
# The grade of John is 100
students = ["Bennet", "Ayaka", "Jean", "Kaeya", "Klee"]
grades = [60, 100, 100, 75, 80]
i = 0
while i < 5:
	print(f"The grade of {students[i]} is {grades[i]}")
	i+=1

# Manipulating the List  
# Built-in methods in python can be used to manipulate the elements in the list
# Adding List items - the append() method allows to insert items to a list 
programs.append('global')
print(programs)

# Deleting List items - the "del" keyword can be used to delete elements in the list
# Add sample elements to be deleted from the list
durations.append(360)
print(durations)

# Delete the last item in the list
del durations[-1]
print(durations)

# Membership checks - the "in" keyword checks if the item/element is in the list
# "in" returns a boolean vale (True/False) if an item is included
print(20 in durations)
print(500 in durations)

# Sorting lists - the sort() method sorts the list alphanumerically, ascending by default
print(names)
names.sort()
print(names)

# Emptying the list - the clear() method is used to empty the contents/elements of the list 
test_list = [1, 3, 5, 7, 9]
print(test_list)
test_list.clear()
print(test_list)

# -----------------------------------------------------------------------------------------
# Dictionaries are used to store data values in key:value pairs
# To create a dictionary in Python, the curly brackets ({}) is used and the key-value pairs are denoted with (key : value)
person1 = {"name" : "Nikolai", 
			"age" : 18, 
			"occupation" : "student", 
			"isEnrolled" : True, 
			"subjects" : ["Python", "SQL", "Django"]
}
print(person1)
# To get the number of key-value pairs in the dictionary, the len() method can be used
print(len(person1))
# Accessing the values in the dictionary
# Using square brackets ([]) can be used and the key/property is used inside the square bracket
print(person1["name"])
# The keys() method will return a list of all the keys in the dictionary 
print(person1.keys())
# The values() method will return a list of all the values in the dictionary
print(person1.values())
# The items() method will return each item in a dictionary as a key-value pair
print(person1.items())

# Adding key-value pairs can be done either putting a new index key and assigning a value
# Can also use the update() method
person1["nationality"] = "Filipino"
person1.update({"fave_food" : "Sinigang"})
print(person1)

# Deleting entries in the dictionary using the pop() method
# Can also use the "del" keyword 
person1.pop("fave_food")
del person1["nationality"]
print(person1)

# clear() method empties the dictionary
person2 = {
	"name" : "John",
	"age" : 25
}
print(person2)
person2.clear()
print(person2)

# Looping through the dictionary 
for key in person1:
	print(f"The value of {key} is {person1[key]}")

# Nested Dictionaries - dictionaries can also be nested inside each other
person3 = {
	"name" : "Monica", 
	"age" : 20, 
	"occupation" : "writer", 
	"isEnrolled" : True, 
	"subjects" : ["Python", "SQL", "Django"]
}
classRoom = {
	"student1" : person1,
	"student2" : person3
}
print(classRoom)

# Mini-exercise
# 1. Create a car dictionary with the following keys
# brand, model, year of make, color
# 2. Print the follwoing statements from the details
# "I own a <brand> <model> and it was made in <year of make>"
# USE SINGLE QUOTATION MARKS TO REFERENCE A KEY
car = {
	"brand" : "Ford",
	"model" : "Everest 3.2",
	"year of make" : 2017
}
print(f"I own a {car['brand']} {car['model']} and it was made in {car['year of make']}")

# Functions 
# Functions in Python are blocks of code that runs when called
# The "def" keyword is used to create a function. The syntax is 
# def <functionName>()

# define a function called my_greeting
def my_greeting():
	# code to be run when my_greeting is called back
	print("Hello User")

# Calling/Invoking a function 
my_greeting()
# Parameters can be added to function to have more control to what the inputs for the function will be 
def greet_user(username):
	# prints out the value of the username parameter
	print(f'Hello, {username}!')

# Arguments are the values that are substituted to the parameters 
greet_user("Jake")
greet_user("Amy")
greet_user("Boyle")

# From a function's perspective:
# A parameter is a variable listed inside the parenthesis in the function definition
# Argument is the value that is sent to the function when it is called

# return statement - the "return" keyword allows the function to return a value
def addition(num1, num2):
	return num1+num2

sum = addition(1, 2)
print(f"The sum is {sum}")
# Direct invocation:
print(f"The sim is {addition(4,5)}")

# Lambda Functions:
# A Lamda function is a small anonymous function that can be used for callbacks
greeting = lambda person : f'hello {person}'
print(greeting("Elsie"))
print(greeting("Anthony"))
# Lambda function with 2 parameters
multiply = lambda a, b : a * b
print(multiply(5, 6))
print(multiply(6, 10))

# Classes in Python
# Classes serves as blueprints to describe the concepts of objects
# Objects have properties and behaviors
# To create a class, the "class" keyword is used along with the class name that starts with an uppercase character/letter
# Example: class Classname()
class Car():
	# properties
	# defining properties use the 'def' keyword
	# self is always requried for each class to reference the 'self' or the object itself
	def __init__(self, brand, model, year_of_make):
		self.brand = brand
		self.model = model
		self.year_of_make = year_of_make
		# Other properties can be added and assigned hard-coded values
		self.fuel = "Gasoline"
		self.fuel_level = 0
	# methods
	# Objects or classes ahould always have method or behavior
	# Self is a parameter to reference the current instance of the class/ access the variables of the calss
	def fill_fuel(self):
		print(f'Current fuel level: {self.fuel_level}')
		print('filling up the fuel tank...')
		self.fuel_level = 100
		print(f'New fuel_level: {self.fuel_level}')
	# methods with parameters
	def drive(self, distance):
		print(f"the car is driven {distance} kilometers.")
		print(f"The fuel level left: {self.fuel_level - distance}")

# Creating a new instance is done by calling the class and provide the arguments
new_car = Car("Nissan", "GT-R", "2019")
# Displaying the attributes can be done using the dot notation
print(f"My car is a {new_car.brand} {new_car.model} and it was made in {new_car.year_of_make}")
# Calling methods of the instance
new_car.fill_fuel()
new_car.drive(50)
