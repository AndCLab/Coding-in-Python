class Camper():
	# Properties
	def __init__(self, name, batch, course_type):
		self.name = name
		self.batch = batch
		self.course_type = course_type
	# Methods
	def career_track(self):
		print(f"Currently enrolled in the {self.course_type}")

	def info(self):
		print(f"My name is {self.name} of batch {self.batch}")


zuitt_camper = Camper("Arno", "2018", "python short course program")
print(f"Camper Name: {zuitt_camper.name}")
print(f"Camper Batch: {zuitt_camper.batch}")
print(f"Camper Course: {zuitt_camper.course_type}")
zuitt_camper.info()
zuitt_camper.career_track()

