# Session 5 Activity 
from abc import ABC, abstractclassmethod

class Animal(ABC):
	@abstractclassmethod
	def eat(self, food):
		pass

	def make_sound(self):
		pass

class Cat(Animal):
	# Properties:
	def __init__(self, Name, Breed, Age):
		super().__init__()
		self._Name = Name
		self._Breed = Breed
		self._Age = Age

	# Methods: Setters
	def set_Name(self, Name):
		self._Name = Name

	def set_Breed(self, Breed):
		self._Breed = Breed

	def set_Age(self, Age):
		self._Age = Age

	# Methods: Getters
	def get_Name(self):
		print(f"This Cat's name is {self._Name}.")

	def get_Breed(self):
		print(f"The Cat's breed is {self._Breed}.")

	def get_Age(self):
		print(f"This Cat is {self._Age} year(s) old.")

	# Implementation of Abstract Method:
	def eat(self, food):
		print(f"Serve me {food}")

	def make_sound(self):
		print(f"Miaow! Nyaw! Nyaaaaa!")

	# Call Method:
	def call(self):
		print(f"{self._Name}, come on!")


class Dog(Animal):
	# Properties:
	def __init__(self, Name, Breed, Age):
		super().__init__()
		self._Name = Name
		self._Breed = Breed
		self._Age = Age

	# Methods: Setters
	def set_Name(self, Name):
		self._Name = Name

	def set_Breed(self, Breed):
		self._Breed = Breed

	def set_Age(self, Age):
		self._Age = Age

	# Methods: Getters
	def get_Name(self):
		print(f"This Dog's name is {self._Name}.")

	def get_Breed(self):
		print(f"The Dog's breed is {self._Breed}.")

	def get_Age(self):
		print(f"This Dog is {self._Age} year(s) old.")

	# Implementation of Abstract Method:
	def eat(self, food):
			print(f"Eaten {food}")

	def make_sound(self):
			print(f"Bark! Woof! Arf!")

	# Call Method:
	def call(self):
		print(f"Here {self._Name}!")


# Test Cases:
dog1 = Dog("Isis", "Dalmatian", 15)
dog1.eat("Steak")
dog1.make_sound()
dog1.call()

cat1 = Cat("Puss", "Persian", 4)
cat1.eat("Tuna")
cat1.make_sound()
cat1.call()

