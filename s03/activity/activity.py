# Accept a year input from the user and determine if it is a leap year or not
# Validation - Strings not allowed and no Zero or Negative values
year = int(input("Please enter a year: "))
if year > 0:
	if year%4 == 0 and year%100 != 0:
		print(f"{year} is a leap year!")
	elif year%400 == 0 and year%100 == 0:
		print(f"{year} is a leap year!")
	else:
		print(f"{year} is not a leap year!")
else:
	print("No zero or negative values!")

# Accept two numbers (row and col) from the user and create a grid of asterisks using the two numbers (row and col)
# Validation - Strings not allowed and no Zero or Negative values
row = int(input("Please enter the value of row: "))
col = int(input("Please enter the value of col: "))

if row > 0 and col > 0:
	for i in range(row):
		for j in range(col):
			print(" * ", end="")
		print("\n")
		
else:
	print("No zero or negative values!")