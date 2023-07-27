# [SECTION] Python class review
class SampleClass():
	def __init__(self, year):
		self.year = year

	def show_year(self):
		print(f"The year is: {self.year}")

myObj = SampleClass(2023)

print(myObj.year)
myObj.show_year()

# [SECTION] Fundamentals of OOP
# Four main fundamental principles in OOP:
# 1.) Encapsulation
# 2.) Inheritance
# 3.) Polymorphism
# 4.) Abstraction

# -----------------------------------------------------------
# [SECTION]
# Encapsulation - a mechanism of wrapping the attributes and codes acting on the methods together as a single unit.
# aka "data hiding"
# an underscore ("_") can be used as a prefix as a warning that an attribute or method is already applying encapsulation so that it cannot be used outside the declared class.
class Person():
	def __init__(self):
		# protected attribute = _name
		self._name = "John Doe"
		self._age = 0xFF

	# Setters are methods to modify properties or attributes of a class
	def set_name(self, name):
		self._name = name

	def set_age(self, age):
		self._age = age
	# Getters are methods to view properties or attributes of a class
	def get_name(self):
		print(f'Name of person: {self._name}')

	def get_age(self):
		print(f'Age of person: {self._age}')

p1 = Person()
# print(p1.name) will result to an attribute error 
print(p1._name)
p1.get_name()
p1.set_name("Jane Doe")
p1.get_name()

# Mini Exercise
# Add another protected attribbute called "age" and and create the necessary getter and setter methods
p1.get_age()
p1.set_age(40)

# --------------------------------------------------------
# [SECTION]
# Inheritance - a way to transfer characteristics from a parent class to a child classes.
# Child classes are derived from the parent (Parent-Child relationship)
# To create an inherited class, in the className definition, add the parent class as the parameter of the child class
# Syntax: class ChildClassName(ParentClassName)
# In this example, the Person class previously defined is a parent class
class Employee(Person):
	def __init__(self, employeeId):
		# super() can be used to invoke the immediate parent class constructor.
		# The getters and setters of the parent class are already accessible
		super().__init__()
		# unique attribute to the Empoyee class
		self._employeeId = employeeId

		# Methods of the Employee class
		def set_employeeId(self, employeeId):
			self._employeeId = _employeeId

		def get_employeeId(self):
			print(f'The employee ID is {self._employeeId}')

	# Details method views the charactersitics
	def get_details(self):
		print(f"{self._employeeId} belongs to {self._name}")

emp1 = Employee("Emp-001")
emp1.get_details()
emp1.get_name()
emp1.get_age()
emp1.set_name("Janeskie Smith")
emp1.set_age(0xAA)

# Mini Exercise 
# 1. Create a new class called Student that inherents Person with the additional attributes and methods
# attributes: Student No, Course, year level
# Methods: Create the necessary getters and setters for each attribute 
# get_detail: prints the ouput"<Student name> is currently in year <year level> taking up <course>

class Student(Person):
	def __init__(self, Student_No, Course, Year_Level):
		super().__init__()
		self._Student_No = Student_No
		self._Course = Course
		self._Year_Level = Year_Level

		def set_Student_No(self, Student_No):
			self._Student_No = Student_No

		def set_Course(self, Course):
			self._Course = Course

		def set_Year_Level(self, Year_Level):
			self._Year_Level = Year_Level

		def get_Student_No(self):
			print(f"Student no is {self._Student_No}")

		def get_Course(self):
			print(f"Student is taking up {self._Course}")

		def get_Year_Level(self):
			print(f"Student is in year {self._Year_Level}")

	def get_details(self):
		print(f"{self._name} is currently in year {self._Year_Level} taking up {self._Course}")
		print(f"{self._name}'s ID number is {self._Student_No}")

# test Case:
stud1 = Student(0xBB, "BSIT", 4)
stud1.get_details()

# --------------------------------------------------------
# [SECTION]
# Polymorphism - the method inherited from the parent class is not always fit for the child class.
# Re-implementation/Overriding of the method can be done in the child class.1
# There are different methods to use polymorphism in Python. 

# Function and Objects - a Function can be created that can take any object allowing polymorphism
class Admin():
	def is_admin(self):
		print(True)

	def user_type(self):
		print('Admin User')

class Customer():
	def is_admin(self):
		print(False)

	def user_type(self):
		print('Customer User')

# Define a test function that will take an object called obj
def test_function(obj):
	obj.is_admin()
	obj.user_type()

user_admin = Admin()
user_customer = Customer()

# Pass the created instance to test function
test_function(user_admin)
test_function(user_customer)

# Polymorphism with Class Methods
# Python uses two different class types in the same way
class TeamLead():
	def occupation(self):
		print('Team Lead')

	def hasAuth(self):
		print(True)

class TeamMember():
	def occupation(self):
		print('Team Member')

	def hasAuth(self):
		print(False)

tl1 = TeamLead()
tm1 = TeamMember()

for person in (tl1, tm1):
	person.occupation()

# Polymorphism with Inheritance
# Polymorphism in python defines methods in child class that have the same name as methods in the parent class.
# "Method Overriding"
class Zuitt():
	def tracks(self):
		print("We are currently offering the tracks(developer career, pi-shape career, and short courses)")

	def num_of_hours(self):
		print("Learn web development in 360 hours!")

class DeveloperCareer(Zuitt):
	# Override the parent's num_of_hours() method
	def num_of_hours(self):
		print("Learn the basics of web development in 240 hours!")

class PiShapedCareer(Zuitt):
	# Override the parent's num_of_hours() method
	def num_of_hours(self):
		print("Learn skills for no-code app development in 140 hours!")

class ShortCourse(Zuitt):
	# Override the parent's num_of_hours() method
	def num_of_hours(self):
		print("Learn advanced topics in web development 20 hours")

course1 = DeveloperCareer()
course2 = PiShapedCareer()
course3 = ShortCourse()

course1.num_of_hours()
course2.num_of_hours()
course3.num_of_hours()

# --------------------------------------------------------
# [SECTION]
# Abstraction 
# An abstract class can be considered as a blueprint for other class.
# Python does not have an abstract keyword, a module is imported/needed to use abstract classes in Python
# Abstract Base Classes (abc)
# The import tells the program to get the abc module of python to be used
from abc import ABC, abstractclassmethod

# The class Polygon() inherits the abstract class module.
class Polygon(ABC):
	# Created an abstract method called print_number_of_sides that needs to be implemented by classes that will inherit Polygon class.
	@abstractclassmethod
	def print_number_of_sides(self):
		# This denotes that the method doesn't do anything
		pass 

class Triangle(Polygon):
	def __init__(self):
		super().__init__()

	# Since the triangle class inherited the polygon class, it must now implement the abstract method
	def print_number_of_sides(self):
		print("This polygon has 3 sides")

class Pentagon(Polygon): 
	def __init__(self):
		super().__init__()

	def print_number_of_sides(self):
		print("This polygon has 5 sides")

shape1 = Triangle()
shape2 = Pentagon()

shape1.print_number_of_sides()
shape2.print_number_of_sides()


