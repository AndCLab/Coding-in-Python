# Capstone Project 1
from abc import ABC, abstractclassmethod

class Person(ABC):
	# Methods
	@abstractclassmethod
	def getFullName(self):
		pass
	def addRequest(self):
		pass
	def checkRequest(self):
		pass
	def addUser(self):
		pass

class Employee(Person):
	# Properties
	def __init__(self, firstName, lastName, email, department):
		super().__init__()
		self._firstName = firstName
		self._lastName = lastName
		self._email = email
		self._department = department

	# Methods: Setters
	def set_firstName(self, firstName):
		self._firstName = _firstName
	def set_lastName(self, lastName):
		self._lastName = lastName
	def set_email(self, email):
		self._email = email 
	def set_department(self, department):
		self._department = department 

	# Methods: Getters
	def get_firstName(self):
		print(f"The employee's first name is {self._firstName}")
	def get_lastName(self):
		print(f"The employee's last name is {self._lastname}")
	def get_email(self):
		print(f"The employee's email is {self._email}")
	def get_department(self):
		print(f"The employee's department is {self._department}")

	# Methods: Abtract
	def getFullName(self):
		return f"{self._firstName} {self._lastName}"
	def addRequest(self):
		return f"Request has been added"
	def checkrequest(self):
		return f"Request has been checked"
	def addUser(self):
		return "User has been added"
	def login(self):
		return f"{self._email} has logged in"
	def logout(self):
		return f"{self._email} has logged out"


class TeamLead(Person):
	# Properties
	def __init__(self, firstName, lastName, email, department):
		super().__init__()
		self._firstName = firstName
		self._lastName = lastName
		self._email = email
		self._department = department
		self._members = set()

	# Methods: Setters
	def set_firstName(self, firstName):
		self._firstName = _firstName
	def set_lastName(self, lastName):
		self._lastName = lastName
	def set_email(self, email):
		self._email = email 
	def set_department(self, department):
		self._department = department 

	# Methods: Getters
	def get_firstName(self):
		print(f"The employee's first name is {self._firstName}")
	def get_lastName(self):
		print(f"The employee's last name is {self._lastname}")
	def get_email(self):
		print(f"The employee's email is {self._email}")
	def get_department(self):
		print(f"The employee's department is {self._department}")

	# Methods: Abstract 
	def getFullName(self):
		return f"{self._firstName} {self._lastName}"
	def addRequest(self):
		return "request has been added"
	def checkRequest(self):
		pass
	def addUser(self):
		pass
	def login(self):
		return f"{self._email} has logged in"
	def logout(self):
		return f"{self._email} has logged out"
	def addMember(self, employee):
		self._members.add(employee)
	def get_members(self):
		return self._members

class Admin(Person):
	# Properties
	def __init__(self, firstName, lastName, email, department):
		super().__init__()
		self._firstName = firstName
		self._lastName = lastName
		self._email = email
		self._department = department

	# Methods: Setters
	def set_firstName(self, firstName):
		self._firstName = _firstName
	def set_lastName(self, lastName):
		self._lastName = lastName
	def set_email(self, email):
		self._email = email 
	def set_department(self, department):
		self._department = department 

	# Methods: Getters
	def get_firstName(self):
		print(f"The employee's first name is {self._firstName}")
	def get_lastName(self):
		print(f"The employee's last name is {self._lastname}")
	def get_email(self):
		print(f"The employee's email is {self._email}")
	def get_department(self):
		print(f"The employee's department is {self._department}")

	# Methods: Abstract 
	def getFullName(self):
		return f"{self._firstName} {self._lastName}"
	def addRequest(self):
		return "Request has been added"
	def checkRequest(self):
		pass
	def addUser(self):
		return "User has been added"
	def login(self):
		return f"{self._email} has logged in"
	def logout(self):
		return f"{self._email} has logged out"

class Request():
	def __init__(self, name, requester, dateRequested):
		self._name = name 
		self._requester = requester
		self._dateRequested = dateRequested 
		self._status = ''

	# Methods: Setters
	def setname(self, name):
		self._name = name 
	def setRequester(self, requester):
		self.requester = requester 
	def setDateRequested(self, dateRequested):
		self._dateRequested = dateRequested 
	def set_Status(self, status):
		self._status = status 

	# Method: Getters
	def getName(self):
		print(f"Name: {self._name}")
	def getRequester(self):
		print(f"Requester: {self._requester}") 
	def getDateRequested(self):
		print(f"Date Requested: {self._dateRequested}")
	def getStatus(self):
		print(f"Status: {self._status}")

	# Methods: Abstract
	def updateRequest(self):
		pass
	def closeRequest(self):
		return f"Request {self._name} has been closed"
	def cancelRequest(self):
		pass

# Test Cases:
employee1 = Employee("John", "Doe", "djohn@mail.com", "Marketing")
employee1 = Employee("John", "Doe", "djohn@mail.com", "Marketing")
employee2 = Employee("Jane", "Smith", "sjane@mail.com", "Marketing")
employee3 = Employee("Robert", "Patterson", "probert@mail.com", "Sales")
employee4 = Employee("Brandon", "Smith", "sbrandon@mail.com", "Sales")
admin1 = Admin("Monika", "Justin", "jmonika@mail.com", "Marketing")
teamLead1 = TeamLead("Michael", "Specter", "smichael@mail.com", "Sales")
req1 = Request("New hire orientation", teamLead1, "27-Jul-2021")
req2 = Request("Laptop repair", employee1, "1-Jul-2021")

assert employee1.getFullName() == "John Doe", "Full name should be John Doe"
assert admin1.getFullName() == "Monika Justin", "Full name should be Monika Justin"
assert teamLead1.getFullName() == "Michael Specter", "Full name should be Michael Specter"
assert employee2.login() == "sjane@mail.com has logged in"
assert employee2.addRequest() == "Request has been added"
assert employee2.logout() == "sjane@mail.com has logged out"

teamLead1.addMember(employee3)
teamLead1.addMember(employee4)
for indiv_emp in teamLead1.get_members():
    print(indiv_emp.getFullName())

assert admin1.addUser() == "User has been added"

req2.set_Status("closed")
print(req2.closeRequest())

